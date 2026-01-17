# Hash_Checker
import colorama
import hashlib
from hashlib import *
colorama.init(autoreset=True)
style = '''\033[31m
                                                 #    #
                                            %%% ##   ##
                                         %%%%% ###%%###
                                        %%%%% ### %%% #
                                      %%%%%% ### %%% ###
                                       %%%% ## %% #######
                                      %%%%% # %% #O#####
                                    %%%%%% # % #########
                                   %%%%% ##### #########
                         ###        %% ####### #########
                %%% ############    ########### ########
             %%%% ############################### #######
           %%%%% ################################## ######
         %%%%%% #################################### #C###
        %%%%%% #####################################  ###
        %%%%% #######################################
       %%%%%% ########################################
    % %%%%%%% ########################################
     %%%%%%%%% #######################################
    %%%%%%%%%% ########################################
 %%% %%%%%%%%   ###### ################################
   %%%%%%%%      ###### #################### ##########      \033[36m@By team YRZ
   % %%%%%%%%        ####### ########### ###### ##########   \033[36m-Hashing Tools
 %%%%%%%%%         #######  ########### ###### ########
%%%%%%%%%%          ##### ###  ######### ####### ######
 %%%%%%%%%%          #### ##               ####### ####
 %%%%%%%%%%%           ## #                  ##### ###
  %%  %% % %%         # ##                      ## ###
    %   %    %        # ###                      # ###
                       # ###                     ## ###
                       # ###                     ## ###
                       # ####                   #### ##
                      ### ###                  ##### ###
                     ####  ###                 ####   ##
                    #####   ###                 ##    ##
                   #####    ####                      ###
                    ##        ###                     ###
                               ####                     ##
                                ####                    ###
                                                        ####
                                                         ##
'''
print(style)                                                         
print('====================================')
print("\033[33m1]- Hash checker \n2]- Hash length \n3]- Hash type") 
print ("\033[33m4]- SHA256 Encrypt\n5]- SHA256 Decrypt\033[37m")
print('====================================')
choose = input("please choose option : ")
if choose == '1':
  print ("This Option For Hash checker")
  hash1 = input("Enter hash [1] : ")
  hash2 = input("Enter hash [2] : ")
  if hash1 == hash2 :
    print ("the hash is Clean ")
  else:
    print ("the hash is Virus ")
#----------------------------------------------------#
if choose == '2':
  print ("This Option For length Hash")
  length = input("Enter your Hash : ")
  print ("Length Hash is " , len(length))
#---------------------------------------------------#
if choose == '3':
  print("This Option For Know Hash ")
  hash = input("Enter the hash : ")
  length = len(hash)
  if length == 32 :
     print ("The Hash is [MD5]")
  if length == 40 :
     print ("The Hash is [SHA1]")
  if length == 64 :
     print ("The Hash is [SHA256]")
if choose == '4' :
  print ("This Option For text to SHA256")
  word = input ("Enter your text : ")
  sha256 = hashlib.sha256(word.encode())
  print (sha256.hexdigest())

if choose == '5':
  print ("This Option For decryption")
  hash = input("Enter your hash : ")
  file = input("write file name : ")
  with open(file ,mode='r') as f :
   for line in f :
     line = line.strip()
     if sha256(line.encode()).hexdigest() == hash :
       print ("[-] Password Found " +line)