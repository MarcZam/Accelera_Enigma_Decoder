# Enigma Decoder

This repository contains a bunch of scripts aimed to construct a virtual enigma machine with a similar functionality as the one used by Nazi Germany in WWII.  
This machine used a series of rotors and a reflector to code and decode messages using an identical set of parameters both for the coding and decoding process, this made the process of coding and decoding much simpler while making the code itself almost uncrackable.

## Rotors

I have created a class for the rotors that consist of lists of tuples that use an indexing sistem to locate the output letters and that rotate whenever a letter is inserted into the machine. This is the way the physical rotors worked in the physical Enigma Machine.
The only difference with the physical device is that you can customize the rotors in the virtual machine to use any language // characters that you want.

(You can also set the letters for the starting position in the rotors whenever you initialize your enigma machine)

## Reflector

The reflector class consists of a list of tuples that are fixed once the machine is created so that every letter in the alphabet has a partner. This device is the one that permits the coding and decoding to be done with the same set on initial parameters as it ensures that the "path" that the letters travel through the machine is identical forwards as backwards.

## Enigma Machine

The final class is an enigma machine that creates 3 rotors, (this is the number of rotors that the standard military machines had) although you can increase or decrease this number if you want, and 1 reflector and it also codes and decodes the messages passed through it.

I hope that if  you do use this repository you enjoy it and you find the ingenuity of this machine as engaging as I do  
Happy ciphering :) 
