     

def getElement2(str1,element):  
    
    res=''
    if( '+' in str1):
         s1=str1.split('+')
         res=s1[element].strip()
    else:
         s1=str1.split('-')
         res=s1[element].strip()

    return res     


def getElement(str1,element):  
    
    symbol=""
    if( '+' in str1):
         s1=str1.split('+')
         symbol=" +"
    else:
         s1=str1.split('-')
         symbol=" -"

    m=True
    maxlen=0

    if(len(s1[0])>len(s1[1])):
        maxlen=len(s1[0])+2
    else:
        maxlen=len(s1[1])+2


    k=""

    if element==0:
        while(True):
            if(len(s1[0])<maxlen):
                s1[0]=" "+s1[0]
            else :
                break
    if element==1:
        while(True):
            if(len(s1[1])<maxlen-3):
                s1[1]=" "+s1[1]
            else :
                break        



    
    if(len(s1[0])==len(s1[1])):
        symbol=symbol.strip()


    if element==1:
         return symbol+s1[1]
    else:    
         return s1[0]     
    

def arithmetic_arranger(str1):
    
    line1=''
    line2=''
    line3=''
    line4=''

    preline1=''
    preline2=''
    preline3=''
    preline4=''


    strSplit=str1



    i=0

    while(True):
        if(i<len(strSplit)):
           
            preline1=getElement2(strSplit[i],0)
            preline2=getElement2(strSplit[i],1)

            if(len(preline1)<len(preline2)):
                k=len(preline2)-len(preline1)+1
                while(True):
                    if(k>0):
                      preline1=' '+preline1
                      k=k-1
                    else:
                      break
                    
            
            elif(len(preline2)<len(preline1)):
                 k=len(preline1)-len(preline2)-1
                 while(True):
                    if(k>0):
                      preline2=' '+preline2
                      k=k-1
                    else:
                      break


            elif(len(preline2)==len(preline1)):
                   preline1=' '+preline1
        


                    

            if('+' in strSplit[i]):                       
                preline2='+ '+preline2
                preline1=' '+preline1
            if('-' in strSplit[i]):                       
                preline2='- '+preline2
                preline1=' '+preline1    


            z=0


            while(True):
                if(z<=len(preline2)-1):
                    preline3=preline3+'-'
                    z=z+1
                else:
                    break  
            
            

            if('+' in strSplit[i]):                       
               h=(int(getElement2(strSplit[i],0))+int(getElement2(strSplit[i],1)))
            if('-' in strSplit[i]):                       
              h=(int(getElement2(strSplit[i],0))-int(getElement2(strSplit[i],1)))
      
            preline4=str(h)


            z=0

            while(True):
                if(z<len(preline1)-3):
                    preline4=' '+preline4
                    z=z+1
                else:
                    break  
                    
            if(i>0):
              preline1='   '+preline1
              preline2='   '+preline2
              preline3='   '+preline3
              preline4='   '+preline4          
                

            line1=line1+preline1
            line2=line2+preline2
            line3=line3+preline3
            line4=line4+preline4

            preline1=''
            preline2=''
            preline3=''
            preline4=''

      
          



            i=i+1



            
        else:
            break
            
            
        
    print(line1)
    print(line2)
    print(line3)
    print(line4)




