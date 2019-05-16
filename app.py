import cv2
from PIL import Image
import numpy as np
empty = ""
while not empty:
    try:
        def enable_transparency():
            from glob import glob
            files_list = glob(r"*.png")
            for file in files_list:
                print(file)
                img = Image.open(file)
                img = img.convert("RGBA")
                datas = img.getdata()
                newData = [item if (item[255] != 255 and item[1] != 255 and item[2] != 255) else (
                    255, 255, 255, 0) for item in datas]
                img.putdata(newData)
                img.save(file, "PNG")

        def show_baby():
            faceCascade = cv2.CascadeClassifier(
                "haarcascade_frontalface_default.xml")
            mask = Image.open("images/baby.png")

            def baby(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 2.1)
                background = Image.fromarray(image)
                for (x, y, w, h) in faces:
                    resized_mask = mask.resize((w + 250, h + 150), Image.ANTIALIAS)
                    offset = (x - 106, y + 60)
                    background.paste(resized_mask, offset, mask=resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor(
                        baby(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR))
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()

        def batman():
            maskPath = "images/bat.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def bat(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 3)
                background = Image.fromarray(image)
                for (x, y, w, h) in faces:
                    resized_mask = mask.resize((w + 40, h + 40), Image.ANTIALIAS)
                    offset = (x - 10, y - 20)
                    background.paste(resized_mask, offset, mask=resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor(
                        bat(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR))
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()

        def baahubali():
            maskPath = "images/bb.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def bb(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 3)
                background = Image.fromarray(image)
                for (x, y, w, h) in faces:
                    resized_mask = mask.resize((w + 200, h + 200), Image.ANTIALIAS)
                    offset = (x - 100, y - 20)
                    background.paste(resized_mask, offset, mask=resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor(
                        bb(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR))
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()

        def bean_anim():
            maskPath = "images/bean_ani.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def bean_a(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 2)
                background = Image.fromarray(image)
                for (x, y, w, h) in faces:
                    resized_mask = mask.resize((w + 200, h + 100), Image.ANTIALIAS)
                    offset = (x - 100, y + 90)
                    background.paste(resized_mask, offset, mask=resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor(
                        bean_a(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR))
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def bean():
            maskPath = "bean.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def bean_(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.5)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 450 , h + 300) , Image.ANTIALIAS )
                    offset = (x - 230, y + 65 )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( bean_(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def hulk():
            maskPath = "images/hulk.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def hlk(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.25)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 600 , h + 400) , Image.ANTIALIAS )
                    offset = (x - 335, y - 130 )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( hlk(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def jerry():
            maskPath = "images/jerry.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def jerry_(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 3)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 250 , h + 200) , Image.ANTIALIAS )
                    offset = (x - 100, y - 30 )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( jerry_(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def mark():
            maskPath = "images/mark.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def mh(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 2)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 300 , h + 250) , Image.ANTIALIAS )
                    offset = (x - 150, y + 80  )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( mh(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def kholi():
            maskPath = "images/rcb.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def vk(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 3)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 220 , h + 200) , Image.ANTIALIAS )
                    offset = (x - 110, y + 30  )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( vk(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def sachin():
            maskPath = "images/sachin.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def srt(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 2)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 600 , h + 250) , Image.ANTIALIAS )
                    offset = (x - 290, y - 50  )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( srt(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()
        
        def warmachine():
            maskPath = "images/warmachine.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            mask = Image.open(maskPath)

            def rhodey(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
                faces = faceCascade.detectMultiScale(gray, 2)	
                background = Image.fromarray(image)
                for (x,y,w,h) in faces:
                    resized_mask = mask.resize( (w + 400 , h + 400) , Image.ANTIALIAS )
                    offset = (x - 220, y - 200  )
                    background.paste(resized_mask, offset, mask = resized_mask)
                return np.asarray(background)

            cap = cv2.VideoCapture(cv2.CAP_ANY)

            while True:
                ret, frame = cap.read()
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                if ret == True:
                    cv2.imshow('Live',  cv2.cvtColor( rhodey(cv2.flip(frame, 1)), cv2.COLOR_RGB2BGR) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release()
            cv2.destroyAllWindows()

        def thug():
            maskPath = "images/thug.png"
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier( cascPath )
            mask = Image.open( maskPath )
            def thug_mask( image ):
                gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
                faces = faceCascade.detectMultiScale( gray, 2 )
                background = Image.fromarray( image )
                for ( x, y, w, h ) in faces:
                    resized_mask = mask.resize( (w , h ), Image.ANTIALIAS )
                    offset = ( x, y )
                    background.paste( resized_mask, offset, mask = resized_mask )
                return np.asarray( background )
            cap = cv2.VideoCapture( cv2.CAP_ANY )
            while True:
                ret, frame = cap.read( )
                if ret == True:
                    cv2.imshow( 'Live', thug_mask( cv2.flip(frame,1) ) )
                    if cv2.waitKey(1) == 27:
                        break
            cap.release( )
            cv2.destroyAllWindows( )

        print( "\n" * 50 )
        choice = int(input("Press\n1 for Baby\n2 for Batman\n3 for Baahubali\n4 for Animated Mr. Bean\n5 for Mr. Bean\n6 for Hulk\n7 for Jerry\n8 for Kohli\n9 for Mark Henry\n10 for Sachin\n11 for Thug Life\n12 for War Machine\n0 for Exiting\nEnter your choice: "))
        
        if choice == 0:
            empty = "not empty"
            exit()
        if choice == 1:
            show_baby()
        if choice == 2:
            batman()
        if choice == 3:
            baahubali()
        if choice == 4:
            bean_anim()
        if choice == 5:
            bean()
        if choice == 6:
            hulk()
        if choice == 7:
            jerry()
        if choice == 8:
            kholi()
        if choice == 9:
            mark()
        if choice == 10:
            sachin()
        if choice == 11:
            thug()
        if choice == 12:
            warmachine()

    except Exception as e:
        pass
        # print(e)