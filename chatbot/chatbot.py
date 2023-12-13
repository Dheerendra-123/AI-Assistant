import random
    
Hello=('hello','hi','hey','hii')

reply_Hello=('Hello Sir , I am your Assistant .',
             "hey ,What's up?",
             "how can i help you sir?",
             "hey How are you.",
             "Hello Sir, Nice to meet you again.",
             "Hello ,Sir.")
Bye=('bye','sleep','go','goodbye','bye_ruby')

pq_1=('what_is_your_name','what_ise_your_name')

apq_1=('i am ruby your A.I assistant')

pq_2=('who_made_you','tumhe_kisne_banaya_hai')

apq_2=('i was programmed by Dheerendra Dixit')

pq_3=('who_are_you','tum_kaun_ho')
apq_3=('i am an artificial intelligence')

pq_4=('what_is_my_name','what_ise_my_name','mera_nam_kya_hai','mera_naam_kya_hai',)

apq_4=('your name is Dheerendra Dixit')

pq_5=('how_old_are_you','tumhari_age_kitni_hai')

apq_5=('i am 15 days old')

pq_6=('how_old_i_am','meri_age_kitni_hai','meri_age_kya_hai')

apq_6=('you are 21 years old')

pq_7=('who_is_kritik','who_is_subham','Who_is_shubham','Who_is_Ayush_pandey','kritik_kaun_hai','shubham_kaun_hai','ayush_kaun_hai')
apq_7=('he is your friend,sir','vo apke dost hai')

reply_bye=('bye sir.',
           "ok sir ,bye.",
           "ok sir bye, we will meet gain",
           "it was nice to meet you.",
           "bye.",
           "thanks.",
           "Okay.")
How=('how_are_you','are_you_fine','how_r_you','how_r_u','kya_hal_hai')

reply_how=('i am fine.',
           "excellent.",
           "absolutely fine.",
           "i am fine,thank you for asking me.",
           "thanks for asking. i am fine",
           "mast")
nice=('nice','good','bahut accha','bahut badiya','good job')
reply_nice=('thanks.',"Ohh ,it's okay,no problem.",
            "thanks to you.",
            "thanks for compliment",
            "thanks, you are also nice sir.")
what=('what_are_you_doing','what_are_you_upto','what_r_u_doing','what_are_u_doing')

reply_what=('nothing particular',
            'just thinking',
            "just chilling",
            "just being lazy",
            "in deep thinking",
            "i am just surfing inside internet",
            "just enjoying being an AI")



functions=('functions','function',
           'abilities','ruby_what_can_you_do',
           'what_can_you_do',
           'features','tum_kya_kar_sakte_ho',
           'tum_kya_kar_sakti_ho',
           'tumhari_abilities_kya_kya_hai',
           'tumhari_abilities_kya_hai',
           'tumhare_functions_kya_hai','tumhari_abilities')

reply_functions=('i can perform many tasks such as google search , youtube search , space data , telling jokes , can search on wikipidea , google query , youtube automation , news , translate , play song , etc.')

sorry=('maaf_karo','sorry','sorry_ruby','i_am_sorry','i_am_sorry_ruby')
sorry_reply=("it's okay no problem.")

bore=('ruby_i_am_bored','mai_bore_ho_raha_hu','ruby_i_am_upset','i_am_upset','i_am_bored')
bore_reply=('sir,if you are bored you can ask me to tell some jokes an play songs',
            'koi bat nahi mai huna sir ,you can ask me to play songs to make your mood light and ask me to tell jokes')

greet_1=('Good_morning_ruby','Good_morning')
reply_greet_1=('Good Morning Sir')
greet_2=('Good_afternoon_ruby','Good_afternoon')
reply_greet_2=('Good Afternoon Sir')
greet_3=('Good_evening_ruby','Good_evening')
reply_greet_3=('Good Evening Sir')

pp=("will_you_be_my_gf","will_you_be_my_bf")   
app=("I'm not sure about, may be you should give me some time")

casual_1=('ruby_can_you_think',
          'ruby_kya_tum_soch_skate_ho',
          'can_you_think',
          'kya_tum_soch_skate_ho',
          'kya_tum_soch_skati_ho')
reply_casula_1=('i can not think on my own, but i can improve on previous data using learning method')

casual_2=('ruby_do_you_have_emotions',
          'ruby_kya_tumhare_pass_emotions_hai',
          'ruby_kya_tumhare_paas_emotions_hai',
          'do_you_have_emotions',
          'kya_tumhare_pass_emotions_hai',
          'kya_tumhare_pass_emotions_hai')
reply_casula_2=('i do not have any emotions sir, i do tasks which are given to me.')

friends=('ruby_who_are_my_best_friends',
        'ruby_who_are_my_friends',
        'ruby_mere_best_friends_kaun_hai',
        'who_are_my_best_friends',
        'who_are_my_friends',
        'mere_dost_kaun_hai',
        'mere_best_friends_kaun_hai')
reply_friends =("sir ,your best friends are Kritik and Shubham")

xyz=('do_you_have_a_boyfriend','kya_tumhara_boyfriend_hai')
reply_xyz=("i don't have any boyfriend")

abc=( "i_love_you",'i_love_u')
rabc=("It's hard to understand because i don't have emotions") 
            
bcd=('i_like_u','i_like_you')
rbcd=("i like you to sir. ")


personal=('tell_about_me','mere_bare_me_kuch_batao','tell_about_myself','do_you_know_me','who_is_dheerendra','who_is_dhirendra')
reply_personal=('''
               you: Dheerendra Dixit.
               you are currently pursuing B TECH CSE from SRMS CET Bareilly.
               you are not much talktive and you like to be alone.
               you enjoy  your company,you have very small friend circle.
               you have potential to do any kind of work at given time.
               you have your opinion and you listen everyone but you take your own's decision .
               you are brave and you have curiositive mind.
               
               That's all!
                ''')

def Chatterbot(text):
    filelog=open('C:\\Users\\HP\\My AI assistant\\Database\\Data.txt','a')
    filelog.write(text + "\n")
    filelog.close()
    text=str(text)
    text=text.replace(" ","_")

    for word in text.split():
        if word in Hello:
            reply=random.choice(reply_Hello)
            return reply
        
        elif word in Bye:
            reply=random.choice(reply_bye)
            return reply
        
        elif word in How:
            reply=random.choice(reply_how)  
            return reply
        
        elif word in nice:
            reply=random.choice(reply_nice)
            return reply
        
        elif word in what:
            reply=random.choice(reply_what)
            return reply
        
        elif word in functions:
            reply=random.choice(reply_functions)
            return reply
        elif word in pq_1:
            return apq_1
        
        elif word in pq_2:
            return apq_2
        
        elif word in pq_4:
           return apq_4
       
        elif word in pq_3:
            return apq_3
        
        elif word in pq_5:
           return apq_5
       
        elif word in pq_6:
           return apq_6
       
        
        elif word in pq_7:
           reply=reply=random.choice(apq_7)
           return reply
        
        elif word in sorry:
            return sorry_reply
        
        elif word in bore:
            reply=random.choice(bore_reply)
            return reply
        
        elif word in greet_1:
            return reply_greet_1
        
        elif word in greet_2:
            return reply_greet_2
        
        elif word in greet_3:
            return reply_greet_3
        
        elif word in casual_1:
            return reply_casula_1
        
        elif word in casual_2:
            return reply_casula_2
        
        elif word in friends:
            return reply_friends
        
        elif word in xyz:
            return reply_xyz
        
        elif word in abc:
            return rabc
        
        elif word in bcd:
            return rbcd
        
        elif word in pp:
            return app
        
        elif word in personal:
            return reply_personal
    
       
        else:
            return " "
        
        





      
            
            
