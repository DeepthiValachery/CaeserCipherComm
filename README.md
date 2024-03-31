# CaeserCipherComm

Program A reads a text file called ‘SleepyBiden.dat’, then encrypts the contents of the file using an one-time pad (OTP) and then saves the encrypted text to a file called ‘Biden.dat’. 

Program B accepts the contents of the ‘Biden.dat’ file and saves it to the hard drive and opens and decrypts the message using the previously sent key, the shared key (Caesar’s shared key) and the OTP decryption algorithm. 
Once decoded, program B should print the contents of ‘Biden.dat’ to the screen.

The key for the OTP should be generated, and an encrypted copy should be sent to program B running on a designated port for key communication on another computer or a separate process (DOS/Terminal window) on the same computer. 
