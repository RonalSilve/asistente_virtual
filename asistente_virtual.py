import sys, os, time, re, webbrowser speech_recognition as sr
from gtts import gTTS
from random import randint
from urllib import request, parse

print('opciones:')
print('[diga]abrir editor de texto',
      '[diga]abrir word','[diga]abrir explorador',
      '[diga]abrir administrador de tareas',
      '[diga]dime un chiste','[diga]buscar en youtube',
      '[diga]buscar en google','[diga]escribir nota',
      sep='\n'
      )

count=0
number=0
lang='es-es'
# obtain audio
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("hola, diga algo:")
        audio = r.listen(source)

        try:
            said=r.recognize_google(audio,language=lang)
            print("usted dijo:" + said)
            if re.match('.brir editor de texto',said):
                tts = gTTS(text="abriendo block de notas", lang='es')
                tts.save("bnota.mp3")
                os.system("start bnota.mp3")
                os.startfile('notepad.exe')
                
            elif re.match('.....bir nota',said):
                tts = gTTS(text="que quiere escribir", lang='es')
                tts.save("nota.mp3")
                os.system("start nota.mp3")
                print('escuchando:')
                audio = r.listen(source)
                
                try:
                    said=r.recognize_google(audio,language=lang)
                    listen=True
                    
                except Exception as e:
                    listen=False
                    print(e)
                    input('no pude escuchar pulse (enter) y repita de nuevo...')
                    
                if listen == True:  
                    file='doc.txt'
                    if os.path.exists(file):
                        while path.exists(file):
                            number+=1
                            newnum=str(number)
                            file='doc'+newnum+'.txt'
                            
                        doc=open(file,'a')
                    else:
                        doc=open(file,'a')
                        
                    for i in said:
                        count+=1
                        doc.write(i)
                        if count==75:
                            doc.write('\n')
                            count=0   
                    doc.close
                    tts = gTTS(text="su nota se a guardado en:"+file, lang='es')
                    tts.save("nsave.mp3")
                    os.system("start nsave.mp3")
                    
            elif re.match('.brir .or',said):
                tts = gTTS(text="abriendo word", lang='es')
                tts.save("word.mp3")
                os.system("start word.mp3")
                os.startfile('winword.exe')
                
            elif re.match('.brir ..plorador',said):
                tts = gTTS(text="abriendo explorador", lang='es')
                tts.save("iexplore.mp3")
                os.system("start iexplore.mp3")
                os.startfile('iexplore.exe')
                
            elif re.match('.brir ....nistrador de tareas',said):
                tts = gTTS(text="abriendo administrador de tareas", lang='es')
                tts.save("Taskmgr.mp3")
                os.system("start Taskmgr.mp3")
                os.startfile('Taskmgr.exe')
                
            elif re.match('........chiste',said):
                random=randint(1,4)
                if random==1:
                    tts = gTTS(text="Llega Pepito al parque, se le acerca "+
                               "un amiguito y le dice:- Eh Pepito, tienes "+
                               "puesto un zapato café y otro negro.Pepito "+
                               "le contesta:- Y eso no es nada, en mi casa"
                               " tengo otro par igualito.", lang='es')
                    tts.save("cuento1.mp3")
                    os.system("start cuento1.mp3")
                    
                elif random==2:
                    tts = gTTS(text="- Veamos, Pepito, ¿qué puedes decirme "+
                               "de la muerte de Cristóbal Colón?- Que lo "+
                               "siento muchísimo, señorita.", lang='es')
                    tts.save("cuento2.mp3")
                    os.system("start cuento2.mp3")
                    
                else:
                    tts = gTTS(text="La profesora le dice a Pepito:- A ver "+
                               "Pepito, si yo digo: fui rica, es pasado, "+
                               "pero si yo digo: soy hermosa, ¿qué es?."+
                               "¡Demasiada imaginación profesora!.", lang='es')
                    tts.save("cuento3.mp3")
                    os.system("start cuento3.mp3")
                    
            elif re.match('.uscar.....ou.ub.',said):
                    tts = gTTS(text="que desea buscar?", lang='es')
                    tts.save("search.mp3")
                    os.system("start search.mp3")
    
                    time.sleep(2)
                    print('buscar:')
                    audio = r.listen(source)
                    try:
                        buscar=r.recognize_google(audio,language=lang)
                        print("usted dijo:" + buscar)
                        listen=True
                        
                    except Exception as e:
                        listen=False
                        print(e)
                        input('no pude escuchar pulse (enter) y repita de nuevo...')
                        
                    if listen == True:
                         tts = gTTS(text="quiere que le muestre la lista o le reprodusca el video?", lang='es')
                         tts.save("youtube.mp3")
                         os.system("start youtube.mp3")
                         time.sleep(4)
                         print('buscar:')
                         audio = r.listen(source)
                         
                         try:
                             said = r.recognize_google(audio,language=lang)
                             print("usted dijo:" + said)
                             listen = True
                         except Exception as e:
                             listen = False
                             print(e)
                             input('no pude escuchar pulse (enter) y repita de nuevo...')
                         if listen == True:
                             query_string = parse.urlencode({"search_query" : buscar})
                             if re.match('........lista',said):           
                                 webbrowser.open("http://www.youtube.com/results?"+query_string)
                             
                             else:
                                 html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
                                 search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                                 webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
                                 
            elif re.match('.uscar.....oogle',said):
                    tts = gTTS(text="que desea buscar?", lang='es')
                    tts.save("search.mp3")
                    os.system("start search.mp3")
    
                    time.sleep(2)
                    print('buscar:')
                    audio = r.listen(source)
                    try:
                        buscar=r.recognize_google(audio,language=lang)
                        print("usted dijo:" + buscar)
                        listen = True
                        
                    except Exception as e:
                        listen = False
                        print(e)
                        input('no pude escuchar pulse (enter) y repita de nuevo...')
                        
                    if listen == True:
                         tts = gTTS(text="buscando en google", lang='es')
                         tts.save("google.mp3")
                         os.system("start google.mp3")
                         time.sleep(2)
                         
                         query_string = parse.urlencode({"q" : buscar})
                         webbrowser.open("https://www.google.com.do/search?"+query_string)
                    else:
                        
                       input('no pude escuchar pulse (enter) y repita de nuevo...')      
                             

            else:
                tts = gTTS(text="la orden no esta en mis opciones o dijo algo mal", lang='es')
                tts.save("error.mp3")
                os.system("start error.mp3")
            input('ok')
            
        except Exception as e:
            print(e)
            input('no pude escuchar pulse (enter) y repita de nuevo...') 
       
