# how-to-export-any-model-from-war-thunder
 a guide on ripping 3d models/assets from war thunder


To do this you will need ninja ripper 2, wiche costs 5$ on patreon there is a free version (ninja ripper 1.7) but im not sure how well it will work for this guide
Ninja ripper website: https://ninjaripper.com
Ninja ripper patreon: https://patreon.com/ninjaripper

First ripping models from in game isn't practical we will use the asset viewer and rip from it, download it here:
https://wiki.warthunder.com/Download_War_Thunder_CDK

This program has every model in wt, at first it seems a bit intemedating but its very simple. 
Once you have ninja ripper, and you unpacked the wt CDK, select the asset viewer cmd, from the wt CDK folder, as the executable program, there are 2 cmds make sure its the asset viewer not the map editor

it shuld look somthing like this: (don't notice my horrible speling lmao)
![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/e3aa614d-a008-4fd4-b553-83c7551fcb55)


Then press launch, it will take a minute or two to load, and sometimes it opens it and moves the window off screen, if you are exprincing that just press Exit in ninja ripper and reopen it should work the second time.
this is how it should look, notice the ninja ripper hud, if you do not see it somthing went wrong

![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/509d2512-f7d8-4d4f-8f49-396dd880ab4d)

Click on all in the bottom left corner, this menu should appear 

![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/72f5fc55-ea69-44fa-a726-a1a43284f74c)

select dynModel
now brows the folders on the left side you will see between map object folders a tanks folder a aircraft folder and a ships folder, all of the game vehicles are in there.
Select a vehicle you want to export, it should show up on screen, like this

![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/474daaaa-2dd5-40de-aaf6-ea0def35d4d7)

If you are exporting a prop aircraft make sure to dissable the prop_dmg nodes on the right side of the screen like this:

![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/8be95712-1fe9-49f3-a977-eb50ba35aee7)

unless of coures you want to use the damged prop.
In the same way you can dissable all of the engine exhaust and gun fire decals, we can remove them in blender but if you preffer to skip that step you can.
Now when you are ready to rip press Print screen.


Open blender, any modern version will do, ninja ripper comes with a blender addon, install it, to install it select edit-> prefrences->addons and install like this:
![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/af3a6e77-a6b7-4456-82f0-0fe7a307d451)

you should have a python script with your ninja ripper install select it and the addon will install.

Now in file-> import select Ninja ripper 2 world space, find the most recent frame in the output directory you selected in the ninja ripper menu, sorting by date enter the most recent folder and you should see a frame_0-frame_1 and so on folders, every frame coresponds to every time you pressed print screen in the asset viewer,
select the most recent frame and press 'a' to select all the files it should look like this:
![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/21e5e40c-7d29-44d8-9ac5-fbd6b4e75e10)

now to you will need to find a FOV_Y value, use this tuturial. this value should work for every model as long as you dont reset the view in the asset viewer(its a button closing and opening will keep the FOV_Y value).
https://www.youtube.com/watch?v=vmBPuWQHmqo
notice that the rip comes with 3 compleatly flat versions of the model so they wont be affected by FOV_Y changes. The real model is around mesh 20-50.

now on the right side input FOV_Y=value that you found and texcord->attribute index UV attrbute index index =2 like this:
![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/d37a4da8-cfda-4730-8529-dabc183d1348)

click import, this will take a second.
the sceane will look like this, notice that im on texture preview mode not object mode:
![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/b9c29728-0110-4a57-92d3-c7b436fe0071)

this reposetory comes with some addons to make this process quicker, feel free to use them:
delete all mats: deleats all matrials in the sceane so the next exporting multiple models wont take up a bunch of spcae, not sure if it dose affect the space, feel free to update it
delete all billboard: removes all meches blelow a certine vertex count, works well but some billboards have some wierdly high vertex countes so they need to be deleted by hand 
delete all objects bellow a highet: pretty self explantory, just make sure to move all origen to center of mass first, works well for getting rid of the bugged squshed meshes.
matrial replace: select a matrial and in the tool menu select replace, it will replace the matrial with a glass matrial, this is for the cockpits and such, when imported thier textur is broken.

now that you cleaned up the model press export FBX, path copy and select the littel box thing near it like this:
![image](https://github.com/tomerla14/how-to-export-any-model-from-war-thunder/assets/45241614/0babfb3a-ff79-41fe-b5ac-5ef8b835190f)
make sure the path mode is on copy!! else when you get rid of the rip files the model textures will brake

Congrats now you have your 3d model from wt! some notes. im not sure why but the export sizes will increas while you export multiple modles from the same blender project, id recemoend restarting blender affter each export. this guide dose not cover the basics of blender, if you are a beginer id recomnd doing the starting steps of the bledner donaght tuturial(just google it its very popular).
id not recomend using these models comertialy seince its aginst tos to rip assets so tred curfuly. If you have any qustions or addtional info, im avilable here welcome to upload an issue. good luck and enjoy the assets!
