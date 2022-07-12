# nao_tutorial1

This repository contains basic information on how to get started with Nao. 

You can find all basic intructions for Nao online (https://www.softbankrobotics.com/emea/en/support/nao-6) or in the Pocket Guide in your Nao box.

When handling Nao always pick him up by holding him around the torso (imagine picking up a young child). Do NOT pull on joints or extremities. 

Always make sure Nao is in a safe place, whether it is charging or you are working with it. Go by the rule of thumb "Would I leave a baby in this spot?" (not near heaters, edges, other moving objects, etc.). Should you see another Nao not being handled correctly, please let the person know.

If this is the first time your Nao robot is used, make sure you charge it fully (indicated by a green light on the power plug). Even if Nao is not unused, it is good to start fully charged and to recharge at the end of a longer session. Nao's battery life is between 45 min to 2h, you can reduce battery usage by turning Nao's motors off, to do this press Nao's button twice. This can be useful, when you are doing longer experiments. The functionalities of the other sensors and cameras remains. 

Your computer should be equipped with some software and packages to interact with Nao, please make sure this is set up before you use Nao for the first time (python 2.7, naoqi). Refer to seperate software set up doc.

Once Nao is charged and your computer is set up, you can place your Nao in a safe spot near you and start it by pressing the round button on its chest once. It takes about 2 min for Nao to turn on, once it's done it will get up and greet you with "ognak gnuk". 

Connecting Nao to Wifi: press the button on Nao's chest once to check the connection status, Nao will either give you an IP address (good) or tell you that it can't connect to a network (not so good). Nao can connect via a personal hotspot you create from your phone. For the first set up you need to connect Nao via the ethernet cable. Connect your laptop to the same network, then press the Nao button once and enter the IP address, that Nao gives you, in your browser. You should be directed to the Softbank robotics interface for your Nao, you will be asked for a username and password, enter nao for both. To make sure you can use your personal hotspot in the future direct to the Wifi section (second item from the left) and select your personal hotspot and enter your password. Now disconnect the ethernet cable from Nao and connect your computer to your personal hotspot. Press Nao's button once again, note that the IP address has now changed as we are using a different Wifi. Enter the new IP address in your browser. Now you should be all set for using Nao from your personal hotspot. 

IMPORTANT: DO NOT UPDATE NAO. All updates should be done centrally.

Now that both Nao and your computer are connected to the same Wifi, you can start interacting with Nao. You can find some example behaviour code in "nao_commands". Open a terminal and make sure you are in a Python 2.7 environment (e.g. conda activate insertnameofpython2env) and then cd to the folder where you saved the code. Try running any of the scripts by typing into your terminal: $ python entercodenamehere.py.

After you have tried out that this works and have made Nao say a few things, it's time to say goodbye. You can turn Nao off by holding its button for 3 seconds (there is an option for a forced turn off if this doesn't work, for this you press the button for 8 seconds, however you have to hold Nao when you do this as it's motors will turn off and it might collapse, this method could also lead to data loss). 

Always store Nao in a safe, locked place. Ensure that there are two keys and that one can be accessed in case you are not available (e.g. by Oksana or your supervisor). 

Have fun using Nao and check out the later tutorials to find out more about what you can do with Nao.



