# Process-mining

World revolves around data. Processed form of information is called data. Every single industry, be it medical or educational institutions, work with a huge amount of data that are classified and processed, to spawn a lot of interesting trends and patterns. With huge amount of data being floating all over, maintaining data privacy and security are seeking importance. Data privacy is the protection of personal data from unauthorized access, thus keeping them safe from thefts and loss. The notion of right to protect data, has created an urge for the creation of pathbreaking data privacy algorithms. 
A keen difference of data privacy and security is that data privacy is about the guidelines for giving access to protected data while data security are the ways and tools for protecting data against unauthorized access.
There are many data privacy algorithms that protect data say, symmetric encryption, asymmetric encryption, authentication and digital signature algorithms. These algorithms provide improved data integrity, security and reliability. These algorithms are widely implemented in two different ways, hardware and software. The algorithms are widely classified based on their usage and applications as follows:
•	Encryption algorithms: symmetric and asymmetric
•	Anonymization techniques: data masking and perturbation
•	Privacy-preserving data algorithms: federated learning, secure muti-party communications.
Let us look in detail about the encryption algorithms.
Symmetric algorithms have a secret shared key for both encryption and decryption. Encryption is the process of converting the readable text to unreadable format at sender’s end while decryption is conversion of this text back to plain text at receiver’s end.  Encryption and decryption are essential in data privacy, as they enhance the security of the data, during communication between the clients and servers. 
A key is an important parameter or a piece of information, that is used to encrypt and decrypt data in cryptographic systems. Due to its high significance, they are usually kept with high confidentiality. Many key management practices lime key rotation, strong key access and secure key storage are practiced to keep the key away from unauthorized access. There are different types of keys namely, shared key, private key, pubic key, session key, symmetric key, key exchange key. 
FEDERATED LEARNING:
Federated Learning:
Federated learning is a distributed machine learning approach that allows training models on decentralized data without transferring the raw data to a central server. Instead, the models are trained locally on the individual devices or servers, and only the model updates are shared and aggregated. Here are some considerations:

Advantages:

Data Privacy: Federated learning helps protect data privacy by keeping the raw data on the local devices and minimizing the exposure of sensitive information. This decentralized approach can be particularly valuable when dealing with sensitive data or complying with privacy regulations.
Reduced Data Transfer: Since only model updates are transmitted, federated learning minimizes the amount of data transferred between devices or servers. This can reduce bandwidth requirements and associated costs.
Collaborative Learning: Federated learning allows multiple parties to collaboratively train models while maintaining privacy. It enables organizations to combine their knowledge and data resources without sharing raw data.
Considerations:

Increased Computational Overhead: Federated learning can introduce additional computational overhead due to the need for coordination between devices or servers. The training process may require more iterations and communication rounds, resulting in longer training times compared to centralized approaches.
Communication and Latency: Communication between devices or servers is crucial in federated learning. The latency and network conditions can impact the training process, particularly in scenarios with unreliable or slow connections.
Device Heterogeneity: Federated learning involves training models on a variety of devices or servers, which can vary in computational capabilities, power, and network connectivity. Managing this heterogeneity and ensuring fair participation can be a challenge.

SYMMETRIC ALGORITHM:
symmetric encryption is a data privacy algorithm. It is a type of encryption where the same key is used for both the encryption and decryption processes. In symmetric encryption, the sender and the recipient of the encrypted data share the same secret key, which is used to transform the plaintext into ciphertext and vice versa.

Symmetric encryption algorithms are widely used to ensure data privacy in various applications. They provide confidentiality by obscuring the content of the data from unauthorized access. The strength of symmetric encryption lies in its efficiency and speed, as it typically requires less computational resources compared to asymmetric encryption algorithms.

However, symmetric encryption faces challenges in securely sharing the secret key between the communicating parties. Key management is a critical aspect to ensure the confidentiality of the shared key and prevent unauthorized access. Additionally, symmetric encryption does not provide inherent mechanisms for non-repudiation or key exchange, which may require additional protocols or algorithms.

Overall, symmetric encryption is an important component of data privacy measures and is often used in combination with other cryptographic techniques to create secure communication channels and protect sensitive information.

What is Symmetric Encryption Used For?
While symmetric encryption is an older method of encryption, it is faster and more efficient than asymmetric encryption, which takes a toll on networks due to performance issues with data size and heavy CPU use. Due to the better performance and faster speed of symmetric encryption (compared to asymmetric), symmetric cryptography is typically used for bulk encryption / encrypting large amounts of data, e.g. for database encryption. In the case of a database, the secret key might only be available to the database itself to encrypt or decrypt. Industry-standard symmetric encryption is also less vulnerable to advances in quantum computing compared to the current standards for asymmetric algorithms (at the time of writing).
Some examples of where symmetric cryptography is used are:
Payment applications, such as card transactions where PII needs to be protected to prevent identity theft or fraudulent charges
Validations to confirm that the sender of a message is who he claims to be
Random number generation or hashing
There are two types of symmetric encryption algorithms:

Block algorithms. Set lengths of bits are encrypted in blocks of electronic data with the use of a specific secret key. As the data is being encrypted, the system holds the data in its memory as it waits for complete blocks.
Stream algorithms. Data is encrypted as it streams instead of being retained in the system’s memory.
ASSYMETRIC ALGORITHM:
Asymmetric encryption algorithms use two different keys for encryption and decryption. The key used for encryption is the public key, and the key used for decryption is the private key. Both the keys must belong to the receiver.
Asymmetric cryptography, also known as public-key cryptography, is a process that uses a pair of related keys -- one public key and one private key -- to encrypt and decrypt a message and protect it from unauthorized access or use.
A public key is a cryptographic key that can be used by any person to encrypt a message so that it can only be decrypted by the intended recipient with their private key. A private key -- also known as a secret key -- is shared only with key's initiator.
When someone wants to send an encrypted message, they can pull the intended recipient's public key from a public directory and use it to encrypt the message before sending it. The recipient of the message can then decrypt the message using their related private key.
If the sender encrypts the message using their private key, the message can be decrypted only using that sender's public key, thus authenticating the sender. These encryption and decryption processes happen automatically; users do not need to physically lock and unlock the message.
Many protocols rely on asymmetric cryptography, including the transport layer security (TLS) and secure sockets layer (SSL) protocols, which make HTTPS possible.
The encryption process is also used in software programs that need to establish a secure connection over an insecure network, such as browsers over the internet, or that need to validate a digital signature.
Increased data security is the primary benefit of asymmetric cryptography. It is the most secure encryption process because users are never required to reveal or share their private keys, thus decreasing the chances of a cybercriminal discovering a user's private key during transmission.
The benefits of asymmetric cryptography include:

The key distribution problem is eliminated because there's no need for exchanging keys.
Security is increased since the private keys don't ever have to be transmitted or revealed to anyone.
The use of digital signatures is enabled so that a recipient can verify that a message comes from a particular sender.
It allows for nonrepudiation so the sender can't deny sending a message.

Key Size:
Symmetric Algorithms: Symmetric algorithms use a single shared key, which typically has a shorter key size compared to asymmetric algorithms. For example, common symmetric algorithms like AES (Advanced Encryption Standard) use key sizes of 128, 192, or 256 bits.
Asymmetric Algorithms: Asymmetric algorithms use a key pair consisting of a public key and a private key. The key sizes for asymmetric algorithms are generally longer compared to symmetric algorithms. For instance, commonly used asymmetric algorithms like RSA or ECC (Elliptic Curve Cryptography) often require key sizes of 2048 bits or higher.
Computational Efficiency:
Symmetric Algorithms: Symmetric encryption and decryption operations are computationally efficient, requiring less processing power compared to asymmetric algorithms. This efficiency makes symmetric algorithms suitable for encrypting and decrypting large amounts of data, such as bulk data transfers or data storage.
Asymmetric Algorithms: Asymmetric encryption and decryption operations are computationally more intensive and slower compared to symmetric algorithms. The longer key sizes and complex mathematical operations involved in asymmetric encryption contribute to the increased computational overhead. As a result, asymmetric algorithms are often used for securing key exchange, digital signatures, and establishing secure communication channels rather than encrypting large volumes of data.
Key Management:
Symmetric Algorithms: Symmetric algorithms require the secure distribution of a shared key between the communicating parties. The challenge lies in securely sharing and managing the secret key, especially in scenarios where there are multiple parties involved or when the key needs to be changed frequently.
Asymmetric Algorithms: Asymmetric algorithms mitigate the key distribution challenge by using a key pair consisting of a public key and a private key. The public key can be freely shared, while the private key is kept secret. Asymmetric algorithms facilitate secure key exchange, authentication, and non-repudiation, eliminating the need for shared secret keys and simplifying key management.
