### Apk (Recommended)
There's also two way of doing this, build from sources or modified .apk.<br/>
Since I don't commit java, we're going with the latter.

You need java installed for this (the same one that you need for Minecraft :>)

* Download [Apktool](https://ibotpeaches.github.io/Apktool/), [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) and osu!droid.apk from it's website
* Create an folder somewhere in your pc and copy all of the file there
* Do `java -jar apktool.jar d droid.apk` and wait till the thing completes
* Open the folder and go to `smali\ru\nsu\ccfit\zuev\osu` and open Notepad++
* Ctrl+F into Notepad++ and go to `Find in Files` tab and do as below. Note that the directory may be different from the screenshot.</br>
![ss](https://yuzumi.please-end.me/IDI8p4.png)
* You will get something like this 
![ss](https://yuzumi.please-end.me/pxYs30.png)
* If you did then put your domain/ip into the `Replace with` box, if not then try again till you find it.
![ss](https://yuzumi.please-end.me/EgdG4F.png)
* After that, search for `secure.gravatar.com` and replace it with your domain
* Okay, we're almost there.
* Go back to the folder that you created and do `java -jar apktool.jar b droid` and the apk should be in `droid\dist` after it completes.
* Do `java -jar signer.jar -a droid\dist\droid.apk --out droid_sign` and there should be `droid-aligned-debugSigned.apk` in the `droid_sign folder`
* and... That's it holy shit thats alot of steps.
* You can now use the modified .apk to connect to the server without doing the Hosts stuff.
