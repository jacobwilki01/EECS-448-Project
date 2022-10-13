## List of things that have been done
    - Create a window
    - Create a background (temporary)
    - Created settings to keep track of 'system' variables
    - Implemented simple main menu
    - Implemented a level with a player
    - Player movement
    - Player-Enviroment Collision
    - Implemented Level changes
    - Implemented speed obstacles
    




## The Game display
    - There are two surfaces in the game: the display surface and the regular surface.
        - `Display surface`: The game window. Anything displayed goes on the display surface. 
        (Only one display surface)
        - `regular surface`: A surface that is not the display surface. It is used to store 
        images and other things that are not displayed on the screen. (Can be many regular surfaces)
        - `blit`: To copy the contents of one surface to another. (Blit is short for block transfer)
