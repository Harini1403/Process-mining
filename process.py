import random
import datetime
import csv
import time
def write_to_csv(process_id, process_name, timestamp, process_time,attribute):
    csv_file_path = 'eventlog.csv'
    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([process_id, process_name, timestamp, process_time, attribute])
def write_to_txt(process_id, process_name, timestamp, process_time,attribute):
    file1 = open("eventlog.txt", "a")
    file1.write("\n") 
    file1.write('{}'.format(idn))
    L = ['\t\t',process_name,'\t\t\t',timestamp,'\t\t']
    file1.writelines(L)
    file1.write(str(process_time))
    file1.write("\t\t")
    file1.write(str(attribute))
    file1.close()    
def para_to_sentence(paragraph):
    current_time = datetime.datetime.now()
    start_time=float(current_time.strftime('%S.%f'))
    print(start_time)
    sentences=paragraph.split('. ')
    sentences = [sentence + ' 'for sentence in sentences[:-1]] + [sentences[-1]]
    num_of_sentences=len(sentences)
    print("NUMBER OF SENTENCES : ",num_of_sentences)
    pname="para_to_sent"
    print("Process name : ",pname)
    global idn
    #idn=random.randint(0,1000)
    print("process id : ",idn)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    print(formatted_time[:-3])
    end_time=float(current_time.strftime('%S.%f'))
    print(end_time)
    process_time=end_time-start_time
    print("process_time : ",process_time)
    nano=process_time*(10**9)
    attr=str(num_of_sentences)+'sentences'
    write_to_txt(idn, pname, formatted_time[:-3], nano,attr)
    write_to_csv(idn, pname, formatted_time[:-3], nano,attr)
    return sentences
def sent_to_words(sentences):
    current_time = datetime.datetime.now()
    start_time=float(current_time.strftime('%S.%f'))
    print(start_time)
    words=[]
    for line in sentences:
        word=line.split()
        for w in word:
            words.append(w)
    number_of_words=len(word)
    print("NUMER OF WORDS : ",number_of_words)
    pname="sent_to_words"
    print("process name : ",pname)
    global idn
    #idn=random.randint(0,1000)
    print("process id : ",idn)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    print(formatted_time[:-3])
    end_time=float(current_time.strftime('%S.%f'))
    print(end_time)
    process_time=end_time-start_time
    nano=process_time*(10**9)
    attr=str(number_of_words)+'words'
    write_to_txt(idn, pname, formatted_time[:-3], nano,attr)
    write_to_csv(idn, pname, formatted_time[:-3], nano,attr)
    return words
def choose_words(words):
    current_time = datetime.datetime.now()
    start_time=float(current_time.strftime('%S.%f'))
    print(start_time)
    number_of_selected_words=random.randint(1,10)
    selected_words=random.sample(words,number_of_selected_words)
    print("number_of_selected_words :",number_of_selected_words)
    pname="choose_words"
    print("Process name : ",pname)
    global idn
    #idn=random.randint(0,1000)
    print("process id : ",idn)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    print(formatted_time[:-3])
    end_time=float(current_time.strftime('%S.%f'))
    print(end_time)
    process_time=end_time-start_time
    nano=process_time*(10**9)
    attr=str(number_of_selected_words)+'selected words'
    write_to_txt(idn, pname, formatted_time[:-3], nano,attr)
    write_to_csv(idn, pname, formatted_time[:-3],nano,attr)
    return selected_words
def form_sentence(selected_words):
    current_time = datetime.datetime.now()
    start_time=float(current_time.strftime('%S.%f'))
    print(start_time)
    number_of_sentences_formed=random.randint(1,10)
    print("NUMBER OF SENTENCES FORMED : ",number_of_sentences_formed)
    count = 0
    sentence=[]
    while (count < number_of_sentences_formed):
        new_sentence=' '.join(random.sample(selected_words,len(selected_words)))
        sentence.append(new_sentence)
        print(new_sentence)
        count=count+1
    print(sentence)
    pname="form_sentence"
    print("process name : ",pname)
    global idn
    #idn=random.randint(0,1000)
    print("process id : ",idn)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    print(formatted_time[:-3])
    end_time=float(current_time.strftime('%S.%f'))
    print(end_time)
    process_time=end_time-start_time
    nano=process_time*(10**9)
    attr=str(number_of_sentences_formed)+'sentences formed'
    write_to_txt(idn, pname, formatted_time[:-3], nano,attr)
    write_to_csv(idn, pname, formatted_time[:-3], nano,attr)
    return sentence
def process(para):
    global idn
    idn=random.randint(0,1000)
    print("process id : ",idn)
    sentence=para_to_sentence(para)
    print("Sentence : ",sentence)
    word=sent_to_words(sentence)
    print("Word : ",word)
    selected_word=choose_words(word)
    print("Selected words : ",selected_word)
    new_sentence=form_sentence(selected_word)
    print("New sentence : ",new_sentence)

def read_file_and_get_paragraphs(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    paragraphs = content.split('\n\n')
    paragraphs = [paragraph.strip() for paragraph in paragraphs]
    file1 = open("eventlog.txt", "a")
    file1.writelines("\npno\t\tpname\t\t\t\t\ttimestamp\t\t\t\t\tduration\t\t\t\t\tattribute")
    return paragraphs

file_path = 'sample.txt'
paragraphs_list = read_file_and_get_paragraphs(file_path)
for i, paragraph in enumerate(paragraphs_list, 1):
    print(f"Paragraph {i}:\n{paragraph}\n") 
    process(paragraph)
    

#para="Hi. My name is XYZ. How are you"
#print("Paragraph : ",paragraph)
#process(paragraph)
