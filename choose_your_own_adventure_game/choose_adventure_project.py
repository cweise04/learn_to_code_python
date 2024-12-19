import sys
import pygame
import textwrap

pygame.init()


screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Choose Your Own Adventure: The Quest for the Treasure of Eldor")

font = pygame.font.SysFont('Century Gothic', 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def get_scaled_font(screen, base_size=36):
    height = screen.get_height()
    font_size = int(height * .03)
    return pygame.font.SysFont('Century Gothic', max(font_size, base_size))

def display_text(lines, options=None):
    screen.fill(BLACK)
    max_width = 1180
    y = 50
    line_spacing = 40
    
    for line in lines:
        wrapped_lines = textwrap.wrap(line, width=90)
        for wrapped_line in wrapped_lines:
            rendered_text = font.render(wrapped_line, True, WHITE)
            screen.blit(rendered_text, (50, y))
            y += line_spacing
            
    if options:
        y += 20
        for idx, option in enumerate(options, start=1):
            rendered_option = font.render(f'{idx}. {option}', True, WHITE) 
            screen.blit(rendered_option, (50, y))
            y += line_spacing
            
    pygame.display.update()
                

def get_user_choice1(options):
    choice = None
    while choice not in options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = options[0]
                elif event.key == pygame.K_2:
                    choice = options[1]
                else:
                    display_text(["Invalid response. Try again. Press 1 or 2."])
    return choice
                    
def get_user_choice2(options):
    choice = None
    while choice not in options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = options[0]
                elif event.key == pygame.K_2:
                    choice = options[1]
                elif event.key == pygame.K_3:
                    choice = options[2]
                else:
                    display_text(["Invalid response. Try again. Press 1, 2 or 3."])
                    
    return choice


def handle_death():
    display_text([ "You died and never found the treasure.", 
    "Game Over!",
    "Try again if you dare."])
    pygame.time.delay(15000)
    pygame.quit()
    sys.exit()

def handle_win():
    display_text([ "Congratulations! You have successfully found the Lost Treasure of Eldor and completed your adventure.",
    "Game Over!",
    "Try again if you dare."])
    pygame.time.delay(15000)
    pygame.quit()
    sys.exit()


def start_of_game():
    intro_text = [
        "Welcome to Choose Your Own Adventure!", 
        "In this game, you will step into the boots of an adventurer on a quest to find the legendary Lost Treasure of Eldor.", 
        "Armed with a mysterious map left by your late father, you embark on an expedition into a jungle filled with danger, secrets, and choices.", 
        "Throughout the game, you will encounter moments where you must make crucial decisions. Sometimes you'll have 2 options, sometimes 3.", 
        "To select a choice, simply press the corresponding keyboard number (1, 2, or 3).", 
        "You'll also encounter story mode sequences. In these moments, sit back and enjoy the unfolding narrative.", 
        "To move on in the story, press the **Enter** key.", 
        "Along your journey, you'll face challenges, uncover ancient secrets, and explore the unknown. Will you find the treasure and escape with your life, or will the jungle claim another victim? The path is uncertain, and danger lurks at every turn.", 
        "Are you ready to begin? Press **S** to start or **E** to quit."
    ]

    
    display_text(intro_text)
    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    display_text(["Starting the game..."])
                    pygame.time.delay(2000)
                    running = False 
                elif event.key == pygame.K_e:
                    display_text(["Exiting game."])
                    pygame.time.delay(2000)
                    pygame.quit()
                    sys.exit()

def wait_for_input():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def game():
    game_on = True
    
    display_text ([
        "After days of travel, you finally arrive at the edge of the jungle. The air is thick with humidity, and the dense canopy ahead casts a shadow over the untamed wilderness. The path is unclear, and the jungle seems to whisper secrets of those who have ventured before you.",
        "The map your father left you has guided you this far, but now, the trail is lost. His notes were clear until this point, but beyond here, it's a mystery—unchartered and untamed.",
        "With a heavy heart, you fold the map and slip it back into your pocket. From this point onward, you are on your own. Your father's legacy has brought you to the jungle’s edge, but the treasure lies deeper, hidden within the shadows of the unknown.",
        "You take a deep breath, your nerves tingling with anticipation. The real adventure begins now.",
        "Do you choose to:",
        "1. Enter the jungle immediately, hoping to cover ground before nightfall.",
        "2. Set up camp for the night and start fresh in the morning."])
    first_choice = None
    while first_choice not in ['Jungle', 'Camp']:
        first_choice = get_user_choice1(['Jungle', 'Camp'])
    
    while game_on:
        
        if first_choice == 'Jungle':
            display_text(["You decided to venture into the jungle before dark. As you trek through the underbrush, you hear strange noises and feel eyes watching you. Suddenly, you reach a fork in the path."])
            wait_for_input()
            
            path_direction = None
            display_text(["At the fork, do you choose to:", 
                "1. Go left, following a trail of strange footprints.",
                "2. Go right, where the path seems clearer but leads deeper into the jungle."])

            while path_direction not in ['Left', 'Right']:
                path_direction = get_user_choice1(['Left', 'Right'])
          
                if path_direction == 'Left':
                    display_text(["The footprints lead you to an abandoned temple. Its doors are ajar, and you feel a strong sense of curiosity."])
                    wait_for_input()

                    temple = None
                    display_text(["Do you choose to:", 
                        "1. Enter the temple",
                        "2. Ignore the temple and keep following the footprints."])
                
                    while temple not in ['Enter', 'Ignore']:
                        temple = get_user_choice1(['Enter', 'Ignore'])
                    
                        if temple == 'Enter':
                            display_text(["You step cautiously into the abandoned temple. The air inside is thick with dust, and the dim light from the outside fades as you move deeper into the shadowy structure. The walls are lined with strange, faded murals depicting long-forgotten kings. You feel an ominous presence, as if the temple itself is watching your every move.",
                            "Suddenly, you hear the grinding sound of stone shifting behind you—the entrance has sealed shut. You're trapped inside.",
                            "The path ahead leads you into a vast chamber with intricate carvings on the walls, depicting scenes of treasure hunters, ancient kings, and valuable artifacts. The air is thick with dust, and a sense of mystery fills the room. In the center, there’s a stone pedestal with a golden idol atop it. Surrounding the pedestal are several tiles, each marked with different symbols. The plaque on the wall reads:",
                            "Only the worthy may pass and claim the treasure. Choose wisely, or face the deadly consequences of greed.",
                            "You examine the symbols on the tiles closely. They seem to correspond to various valuable treasures that could be hidden within the temple. Each tile may lead you closer to the prize—or lead to danger."])
                            wait_for_input()

                            temple_puzzle = None

                            display_text(["Do you choose to:", 
                                "1. Step on the tile marked with the symbol of a radiant gem.", 
                                "2. Step on the tile marked with the symbol of an ancient chest.",
                                "3. Step on the tile marked with the symbol of a golden crown."])
                    
                            while temple_puzzle not in ["Gem","Chest", "Crown"]:
                                temple_puzzle = get_user_choice2(['Gem', 'Chest', 'Crown'])
                        
                                if temple_puzzle == 'Gem':
                                    display_text(["You step onto the tile with the gem symbol, believing it to represent wealth and fortune. For a moment, the room stays still. Then, the floor beneath you begins to tremble, and the walls start to close in, slowly crushing the room from both sides."])
                                    wait_for_input()
                                    
                                    room_choice = None
                                    display_text(["Do you choose to:", 
                                                 "1. Run back and choose another tile.",
                                                 "2. Look for a hidden lever or switch in the walls."])
                                    while room_choice not in['Tile', 'Switch']:
                                        room_choice = get_user_choice1(['Tile', 'Switch'])
                                    
                                        if room_choice == 'Tile':
                                            display_text(["You quickly jump off the tile, hoping to avoid the trap. But the walls continue to close in, inching closer until the room offers no escape. You scramble for a way out, but it’s too late—the walls close in completely, and you are crushed."])
                                            game_on = handle_death()
                                            wait_for_input()
                                            
                                        elif room_choice == 'Switch':
                                            display_text(['You search the room frantically and discover a hidden indentation in the wall. Pressing it opens a secret door, leading you to a narrow, dark corridor and escaping the room that was closing in on you.',
                                            'In the corridor, the path twists and turns, eventually leading to a massive stone door covered in intricate carvings. The door bears a riddle, which must be solved to proceed.',
                                            '"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"'])
                                            wait_for_input()
                                            
                                            corridor = None
                                            display_text(["Do you choose to:", 
                                                "1. Stop and answer the riddle.",
                                                "2. Search the corridor for more clues."])

                                            while corridor not in ['Riddle', 'Search', 'Force']:
                                                corridor = get_user_choice2(['Riddle', 'Search'])
                                                
                                                if corridor == 'Riddle':
                                                    display_text(["You confidently answer the riddle: 'an echo.' The glowing runes flare brightly, and the door begins to grind open.",
                                                    "But as the door creaks ajar, the carvings spring to life. Stone serpents emerge, their fangs glistening like shards of obsidian.",
                                                    "Your answer has triggered a deadly trap—an ancient safeguard designed to punish intruders who rely on wit alone.",
                                                    "The serpents strike, their stone fangs sinking into your body as darkness consumes you.",])
                                                    wait_for_input()
                                                    game_on = handle_death()
                                                    
                                                elif corridor == 'Search':
                                                    display_text(["You decide to explore the corridor, ignoring the riddle for now. As you search, you notice faint markings on the wall, almost hidden in the dim light.",
                                                    "The markings form a pattern, leading to a loose stone near the floor. Pressing it reveals a hidden compartment containing a small, ancient artifact.",
                                                    "When you place the artifact into a slot on the massive stone door, the glowing runes fade, and the door silently swings open.",
                                                    "Inside, you find a hidden chamber filled with piles of gold, glittering jewels, and ancient artifacts. The Lost Treasure of Eldor lies before you, untouched for centuries.",
                                                    "Your cleverness and caution have rewarded you with the treasure. You take it home and celebrate your victory."])
                                                    wait_for_input()
                                                    game_on = handle_win()
                                                    
                                                elif corridor == 'Force':
                                                    display_text([
                                                    "You attempt to force the door open with brute strength. The glowing runes flicker violently, and the carvings seem to shift, reacting to your defiance.",
                                                    "Suddenly, the ground beneath you trembles, and the walls close in. A crushing noise fills the air as the ancient mechanisms spring to life.",
                                                    "Your reckless actions have triggered the corridor's fail-safe. You are crushed as the walls seal shut, ending your adventure.",
                                                    "You have died."])
                                                    wait_for_input()
                                                    game_on = handle_death()
                                                    

                                elif temple_puzzle == 'Chest':
                                    display_text(["You cautiously step onto the tile with the chest symbol. The room shakes slightly, but nothing seems to happen. After a moment, the pedestal in the center of the room glows faintly, and the lid of the chest opens, revealing a treasure map inside. It's partially torn, but you can make out markings that could lead to the Lost Treasure of Eldor."])
                                    wait_for_input()
                                    
                                    temple_chest = None
                                    display_text(["Do you choose to:", 
                                        "1. Quickly take the treasure map.",
                                        "2. Examine the chest further."])
                                    
                                    while temple_chest not in ['Take', 'Examine']:
                                        temple_chest = get_user_choice1(['Take', 'Examine'])
                                        if temple_chest == 'Take':
                                            display_text(["The moment you touch the map, the room shudders, and a trapdoor opens beneath your feet. You fall to your death into a dark pit below with spikes sticking up."])
                                            wait_for_input()
                                            game_on = handle_death()
                        
                                        elif temple_chest == 'Examine':
                                            display_text(["You open the chest completely and discover a hidden compartment beneath the false bottom. Inside, you find a golden artifact—perhaps a key or symbol related to the treasure’s final location. With the artifact in hand, you begin to look around the room for a way out. As you approach the pedestal, you notice a strange indentation in the stone directly beneath it—a keyhole. You realize that the artifact may fit into this keyhole, but the consequences of doing so are unclear. The artifact seems to pulse with energy, almost as if it's urging you forward.",
                                            "You place the artifact into the keyhole, and as it clicks into place, the ground shakes. A deep rumbling echoes throughout the chamber as the walls begin to move, opening a door leading down a corridor.",
                                            "You brace yourself as you continue forward. As you go down the corridor, you enter a room with two passages. The first passage is a gleaming golden passage with lots of light and everything made of gold, leading upward. The second passage is a dark, shadowy passage leading downward, where eerie whispers can be heard.",
                                            "The artifact pulses again, as if signaling that only one path will lead to the treasure, while the other may lead to your doom."])
                                            wait_for_input()
                                            
                                            temple_passageway = None
                                            display_text(["Do you choose to:", 
                                                "1. Choose the golden passage.",
                                                "2. Choose the shadowy passage."])

                                            while temple_passageway not in ['Golden', 'Shadowy']:
                                                temple_passageway= get_user_choice1(['Golden', 'Shadowy'])
                                                    
                                                if temple_passageway == 'Golden':
                                                    display_text(["You step carefully onto the golden path, your heart racing with excitement. But as you move forward, the walls begin to close in once again. The ground beneath you trembles, and the golden path seems to shift and distort. It's a trap!",
                                                    "A massive stone block drops from above, trapping you in place. You struggle, but it’s too late—the crushing weight of the block sends you plummeting into darkness."])
                                                    wait_for_input()
                                                    game_on = handle_death()
                                                    
                                                elif temple_passageway == 'Shadowy':                                                        
                                                    display_text(["You take a deep breath and step into the shadowy passage. The eerie whispers grow louder, but you press on. The path twists, and soon you find yourself standing before another door—a massive stone door with intricate markings and a single keyhole in the center.",
                                                    "You insert the golden artifact into the keyhole. With a loud click, the door creaks open, revealing a hidden chamber. And there it is, gleaming in the dim light—the Lost Treasure of Eldor."])
                                                    wait_for_input()
                                                    game_on = handle_death()
                            
                                elif temple_puzzle == 'Crown':
                                    display_text(["You step onto the tile with the crown symbol, thinking it represents leadership and the rule of a powerful king. The floor seems stable for a moment, but then you hear a faint clicking noise. A set of spikes begins to emerge from the walls, aiming directly at you."])
                                    wait_for_input()
                                    
                                    temple_crown = None
                                    display_text(["Do you choose to:", 
                                        "1. Dodge the spikes and step off the tile.",
                                        "2. Try to find a way to disarm the trap."])
                                    
                                    while temple_crown not in ['Dodge', 'Disarm']:
                                        temple_crown = get_user_choice1(['Dodge', 'Disarm'])
                                        
                                        if temple_crown == 'Dodge':
                                            display_text(["With a burst of adrenaline, you leap to the side just in time, narrowly avoiding the deadly spikes that shoot from the walls. The hiss of metal scraping against stone echoes in your ears as you land hard, breathless but alive. The crown tile remains glowing ominously, the spikes retracting back into their hidden slots as if waiting for another misstep.",
                                            "You wipe the sweat from your brow, heart still pounding. You know now that every move must be precise if you’re to survive this ancient temple.",
                                            "You step back, feeling the weight of the temple's ancient tricks and traps closing in on you. The air is heavy with dust, and you realize that relying solely on the floor tiles may not be the wisest strategy. The temple is a puzzle in itself, and its secrets may be lurking elsewhere—above, below, or around you.",
                                            "You stop, your eyes scanning the room. Perhaps there's more to this chamber than meets the eye.",
                                            "As you look around the room you see 3 potential paths you could try or could they be 3 potential traps."])
                                            wait_for_input()
                                                
                                            three_paths = None
                                            display_text(["Your 3 potential paths are: 1. Search the walls. 2. Examine the ceiling. Or 3. Look for a hidden passage in the corners of the room.",
                                                "Do you choose to:",
                                                "1. Search the walls.",
                                                "2. Examine the ceiling.",
                                                "3. Look for a hidden passage in the corners of the room."])
                                             
                                            while three_paths not in ['Walls', 'Ceiling', 'Corners']:
                                                three_paths = get_user_choice2   
                                                
                                                if three_paths == "Walls":
                                                    display_text(["You run your hands along the cold stone walls, feeling for any unusual bumps or cracks. As you press on different sections, one stone shifts slightly under your fingers. It feels loose, as if it were designed to move."])
                                                    wait_for_input()
                                                    
                                                    temple_stone = None
                                                    display_text(["Do you choose to:",
                                                        "1. Press the loose stone further and see if it triggers something.",
                                                        "2. Leave it alone and explore another part of the wall."])
                                                    
                                                    while temple_stone not in ['Press', 'Leave']:
                                                        temple_stone = get_user_choice1  
                                                        if temple_stone == "Press":
                                                            display_text(["Cautiously, you press the stone deeper into the wall. At first, nothing happens, but then you hear a soft click. A sudden chill runs down your spine. Before you can react, steel clamps snap around your wrist, trapping your hand against the wall.",
                                                            "A hiss fills the air—cold, sharp, and ominous. You glance up in horror as small nozzles emerge from the wall above the stone, releasing a faint mist. Your heart pounds as the acrid smell of toxic gas hits your nostrils.",
                                                            "You try to pull your hand free, but the clamp holds tight. Panic surges through you as your vision starts to blur, and a burning sensation spreads through your lungs. The gas is taking effect—there's no escape.",
                                                            "As your strength fades, you realize this was a trap meant to keep treasure seekers like you from proceeding. Your hand remains pinned, and the gas consumes you."])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                                        
                                                        elif temple_stone == "Leave":
                                                            display_text(["Something in your gut tells you not to press your luck. You step back, deciding that the stone might not hold the solution you need. Instead, you continue along the wall, carefully feeling for any other clues or mechanisms.",
                                                            "In the far corner, you find a barely perceptible seam—a crack in the wall that seems too deliberate to be a natural flaw. Pushing gently, a section of the wall slides away, revealing a narrow hidden passage.",
                                                            "The passage narrows as you move forward, the air thick with dust and the scent of long-forgotten secrets. Your footsteps echo off the stone walls, growing louder in the oppressive silence. After what feels like an eternity, you arrive at the end of the passage—a large, ornate chamber with high ceilings and walls adorned with faded murals of ancient treasure hunters.",
                                                            "At the center of the room stands an elaborate stone altar, covered in intricate carvings. On top of the altar lies a weathered chest, its edges chipped and covered in ancient moss. To the left, a large stone door blocks your exit.",
                                                            "A faint humming sound fills the air, and your eyes are drawn to the strange glow coming from the chest. You approach, hesitant but determined. On the stone door, an inscription catches your eye:",
                                                            "Where shadows dwell, the light will reveal what’s hidden. Only those who seek with more than their eyes may find it.",
                                                            "The room is eerily still, and there's an unsettling sense that something is watching you. You realize the inscription could be the key, but it doesn’t make sense right away."])
                                                            wait_for_input()
                                                            
                                                        temple_clue = None
                                                        display_text(["Do you choose to:", 
                                                            "1. Look around the room for a hidden light source or another clue.",
                                                            "2. Open the chest without further investigation."])
                                                    
                                                        while temple_clue not in ['Look', 'Open']:
                                                            temple_clue = get_user_choice1(['Look', 'Open'])
                                                    
                                                            if temple_clue == "Look":
                                                                display_text(["You step back from the chest, the inscription repeating in your mind: 'Where shadows dwell, the light will reveal what’s hidden.' You scan the room, looking for any unusual features.",
                                                                "The walls are covered in faded murals, but one near the far side of the chamber catches your attention. It depicts a scene of an ancient explorer entering a treasure room, and in the shadows of the artwork, there’s a faint glimmer of light.",
                                                                "You step toward the mural and notice something odd about the area where the light seems to be coming from—it’s not a painting at all. Instead, it's a small indentation in the stone wall, cleverly disguised. You press it gently, and a faint click echoes through the chamber.",
                                                                "Suddenly, a beam of light shoots out from the wall, illuminating the room. The chest you were about to open is now bathed in the glow, but something else catches your eye—the floor beneath the chest shifts, revealing a hidden compartment carved into the stone slab.",
                                                                "Kneeling down, you carefully lift the lid of the compartment and find an ancient key—its intricate design matching the carvings on the walls. Next to the key lies a note, fragile with age, but still legible:",
                                                                "'The final key to the treasure lies beyond this room, where light and shadow meet. Use this key, and the path shall be revealed.'",
                                                                "You turn back toward the chamber, the key in hand, when you notice a small keyhole embedded in one of the nearby pillars. The carvings around the keyhole match the designs on the key perfectly. With trembling hands, you insert the key and turn it slowly.",
                                                                "Click.",
                                                                "The ground shakes for a moment, and then the wall in front of you begins to shift. Stones slide aside, revealing a narrow passage that glows with a golden hue. You can hardly believe it, but as you step inside, the passage opens into a magnificent chamber.",
                                                                "The treasure is here. Piles of gold, gleaming jewels, and ancient artifacts are scattered across the room, undisturbed for centuries. At the center, a golden idol, encrusted with gemstones, sits on a raised platform—the heart of the treasure you've sought for so long."])
                                                                wait_for_input()
                                                                game_on = handle_win()
                                                            
                                                            elif temple_clue == "Open":
                                                                display_text(["You decide to ignore the inscription and open the chest, eager for the treasure inside. As you lift the lid, you hear a click, and the chest immediately begins to shake violently.",
                                                                "Before you can react, a cloud of noxious green gas billows out of the chest, filling the air around you. You stagger backward, coughing, trying to wave the gas away, but it's no use. Your vision blurs, and the room seems to spin.",
                                                                "Suddenly, something moves in the shadows near the chest. You blink, trying to focus, but it's too late. A large, snake-like creature slithers out from the chest, its scales glistening in the dim light. Its eyes glow with an eerie, predatory light, and with a swift, deadly strike, it lunges toward you.",
                                                                "You try to dodge, but the gas has weakened your movements. The creature's fangs sink into your leg, and a burning sensation spreads through your body. You collapse to the ground, the world fading as the poison takes hold.",
                                                                "The chest was a trap, and now the treasure, whatever it may be, is lost to you forever."])
                                                                wait_for_input()
                                                                game_on = handle_death()
                            
                                                elif three_paths == "Ceiling":
                                                    display_text(["You tilt your head up, squinting at the ceiling. Among the cracks and worn stone, you notice faint carvings—symbols that resemble those on the tiles below. Could they be connected? As you study them, you realize the patterns are inverted versions of the floor tiles.",
                                                    "Following the ceiling's guide, you step onto the mirrored tile. As you press down, a soft click echoes through the chamber. The tile glows faintly, and the door across the room slowly creaks open, revealing a hidden passage. You smile, realizing you've cracked the temple's puzzle and can now move deeper into the treasure vault.",
                                                    "You step cautiously toward the newly revealed passage. The air inside the corridor is cooler and damp with the scent of ancient stone. The dim light from the chamber behind you fades as you venture further into the tunnel. Your heart races, feeling like you're getting very close to the treasure.",
                                                    "As you move deeper, the passage widens into a vast underground chamber. The walls are lined with towering stone columns, each carved with intricate depictions of explorers, treasure, and mysterious symbols. In the center of the chamber stands a massive stone pedestal, and atop it, a golden chest gleams in the flickering torchlight.",
                                                    "But something feels off. The floor between you and the chest is covered with more tiles, each inscribed with different symbols—many of which match the ones you've seen before. A faint draft whispers through the chamber, and you can’t shake the feeling that another trap is waiting."])
                                                    wait_for_input()
                                                    
                                                    no_way_out = None
                                                    display_text(["Do you choose to:", 
                                                        "1. Carefully inspect the floor for traps.",
                                                        "2. Walk directly to the chest, confident you've solved the temple's riddles.",
                                                        "3. Search the chamber for hidden clues or switches."])
                                                    
                                                    while no_way_out not in ['Inspect', 'Walk', 'Look']:
                                                        no_way_out = get_user_choice2(['Inspect', 'Walk', 'Look'])
                                                        
                                                        if no_way_out == "Inspect":
                                                            display_text(["You crouch and carefully examine each tile. You notice subtle differences—the edges of certain tiles are slightly raised, and others seem worn from centuries of use. You deduce that the raised tiles are pressure-sensitive traps. Slowly, you step only on the worn, safer tiles.",
                                                            "But just as you near the chest, your foot presses down ever so slightly on an unnoticed raised tile. A split second later, sharp darts shoot out from the walls, striking you in the back before you can react. You collapse to the ground, your vision blurring as the chamber spins."])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                                        
                                                        elif no_way_out == "Walk":
                                                            display_text(["You march confidently across the room, certain that you’ve solved all of the temple’s riddles. The chest is right in front of you, waiting to be opened. But just as your hand touches the lid, a soft click sounds beneath your feet.",
                                                            "Without warning, a barrage of poisoned darts flies out from hidden holes in the walls, striking you from every direction. You gasp in pain, feeling the toxins work fast. Your vision darkens, and your legs give way as you fall to the floor."])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                            
                                                        elif no_way_out == "Look":
                                                            display_text(["You decide there must be another way—something hidden in the chamber that can help you safely reach the treasure. After all, these temples are notorious for tricks. You begin to examine the walls and floor, searching for hidden clues or switches.",
                                                            "As you run your hand along the cold stone, you feel a slight depression in the wall. Without thinking, you press it, triggering a hidden mechanism. Instead of revealing a secret, a volley of poisoned darts bursts from the walls. They hit you all at once, the poison working quickly. You stumble, your body betraying you as you fall to the ground."])
                                                            wait_for_input()
                                                            game_on = handle_death()

                                                elif three_paths == "Corners":
                                                    display_text(["You cautiously approach the key, eyes scanning the floor and walls for any signs of danger. Your instincts tell you to be careful, but the allure of the golden artifact is too strong to resist. As your hand wraps around the cool metal of the key, nothing happens at first.",
                                                    "But then, the moment you lift the key off the pedestal, a deafening click echoes through the room. The walls begin to tremble violently, and the floor shifts beneath your feet. Before you can react, the ceiling starts to lower, revealing a network of small holes along the edges of the walls.",
                                                    "With a hiss, a barrage of poisoned darts shoots out from every corner, raining down on you from all sides. You try to dodge, but the darts are too fast, too many. One after another, they pierce your skin. You feel the burning sting of the poison coursing through your veins.",
                                                    "The ceiling continues to descend slowly, adding to the terror. Your limbs feel heavy, your vision blurs, and within moments, the world fades to black."])
                                                    wait_for_input()
                                                    game_on = handle_death()

                                        elif temple_crown == "Disarm":
                                            display_text(["You quickly assess the situation, and your instincts scream at you to find a way to stop the trap before the spikes reach you. You frantically search the walls for any hidden levers or panels. Your eyes catch sight of a small, almost imperceptible panel near the edge of the floor, slightly out of view but within reach.",
                                            "With no time to lose, you lunge toward it, pressing your hand against the stone to reveal the hidden mechanism. A lever appears, and you yank it down with all your strength, hoping to stop the deadly spikes in their tracks.",
                                            "For a moment, the spikes halt, their deadly points mere inches from you. Your heart races, and you breathe a sigh of relief, thinking you’ve narrowly escaped death. But just as the tension begins to ease, you hear a loud, mechanical whirring sound coming from above.",
                                            "Too late, you realize that the trap you’ve disarmed wasn’t fully disabled—it triggered an even deadlier secondary mechanism. The ceiling above you begins to lower at an alarming speed, and before you can react, massive stone blocks descend, trapping you in the chamber.",
                                            "You struggle to escape, but the walls close in too quickly. The pressure of the falling stones crushes you under their weight."])
                                            wait_for_input()
                                            game_on = handle_death()

                        elif temple == "Ignore":
                            display_text(["You decide to ignore the temple’s ominous presence and the dangers lurking within. The footsteps you’ve been following seem like a safer route, so you turn your back on the mysterious structure and press on.",
                            "As you walk deeper into the jungle, the sound of the footsteps grows clearer, and you start to wonder who—or what—is leaving them. The path is dense with vegetation, and the air grows thicker with humidity. The footsteps continue to echo, drawing you further into the wild.",
                            "After hours of walking, the footsteps suddenly stop. Just as the sun is going down and it's getting dark, you find yourself standing at the edge of a dark, cavernous opening in the jungle, hidden behind thick vines and overgrown trees. The air here feels colder, and the shadows seem to stretch unnaturally long.",
                            "You peer inside, but the darkness is almost absolute. The footsteps seem to have disappeared."])
                            wait_for_input()
                            
                            cave = None
                            display_text(["Do you choose to:",
                                "1. Enter the cave.",
                                "2. Set up camp."])

                            while cave not in['Enter', 'Set Up']:
                                cave = get_user_choice1(['Enter', 'Set Up'])
                                if cave == "Enter":
                                    display_text(["You take a step into the cave, your torch flickering as you descend into the darkness. The walls are covered in glowing moss, and the air smells damp. The further you go, the more oppressive the silence becomes. The footsteps that guided you here have vanished, but you feel a strange compulsion to keep going deeper.",
                                    "After what feels like an eternity, you arrive at a vast underground chamber. It’s filled with ancient ruins—crumbling stone pillars, scattered bones, and an eerie stillness. In the center of the room stands an ornate chest, seemingly untouched by time. The air feels thick with anticipation as you move toward it, your heart racing. Could this be the treasure you've been seeking?",
                                    "As you approach the chest, you notice strange markings carved into the stone floor, surrounding it in a perfect circle. Something about the symbols feels wrong, as though they were meant to keep something in, not out. The chest beckons, its golden trim glinting in the low light."])
                                    wait_for_input()
                                    
                                    cave_choice = None
                                    display_text(["Do you:",
                                        "1. Open the chest.",
                                        "2. Examine the markings on the cave floor.",
                                        "3. Leave the cave."])
                                    
                                    if cave_choice == "Open":
                                        display_text(["You place your hands on the chest's heavy lid and push. The moment it opens, a cloud of dust billows into the air, and a low rumbling sound fills the chamber. Before you can react, the walls begin to shake violently, and you hear the sound of metal scraping on stone.",
                                        "Suddenly, the chest seems to collapse in on itself, a horrifying mechanism activated by your touch. The lid slams shut, trapping your hands inside. A sharp pain shoots up your arms as the chest begins to constrict around you.",
                                        "You try to pull away, but it's no use—the chest continues to tighten, and the air in the cave becomes thick with a suffocating fog. The last thing you hear is a low hiss as the mist begins to overwhelm you, choking off your breath. Your vision fades as you lose consciousness, and your body is slowly crushed within the trap."])
                                        wait_for_input()
                                        game_on = handle_death()

                                    elif cave_choice == "Examine":
                                        display_text(["You kneel down to inspect the markings, your fingers tracing the strange symbols etched into the stone. The patterns seem to shift under your touch, and a cold shiver runs down your spine. The symbols are ancient, possibly warning signs to anyone foolish enough to enter this chamber.",
                                        "Suddenly, as your fingers press deeper into one of the symbols, you hear a loud click. The ground beneath you trembles, and you realize too late that you’ve triggered a trap. The floor cracks open around you, and a swarm of sharp spikes shoots up from the ground below.",
                                        "You have no time to react as the spikes impale you from all sides, your body swiftly pierced by their razor tips."])
                                        wait_for_input()
                                        game_on = handle_death()              

                                elif cave == 'Set Up':
                                    display_text(["The darkening jungle makes you reconsider your course of action. You can barely see where you're going, and the path ahead seems treacherous. You decide to set up camp for the night, hoping the morning light will give you a better chance at finding the treasure.",
                                    "You gather some dry wood and start a fire, the flames crackling in the growing cold. The shadows around you stretch longer, but you feel a sense of safety as you huddle by the warmth of the fire. The forest seems quieter at night, the wildlife eerily absent.",
                                    "The fire flickers and crackles, casting strange shadows across the jungle. You lie down to sleep, the fire’s warmth slowly lulling you into a sense of security. As you drift into slumber, the jungle around you seems to come alive with distant whispers. The air feels thick, oppressive.",                                        
                                    "Your dreams are filled with strange visions—an ancient chest, a golden amulet, and a hidden treasure far beneath the jungle floor. The treasure is close, but it seems just out of reach, like a fleeting dream. As the night deepens, your dreams grow darker and more frantic.",
                                    "You wake to the sound of rustling in the bushes, but when you sit up, there’s nothing there. The fire has gone out, and the jungle is unnervingly quiet. A sense of dread fills the air. You get up to check your surroundings, but before you can react, a low growl echoes from the darkness.",
                                    "Suddenly, a pair of glowing eyes peer from the underbrush, and you feel a cold shiver crawl down your spine. Before you can draw your weapon or react, the jungle around you bursts to life. A creature, something inhuman, leaps from the shadows and tackles you to the ground.",
                                    "You fight back with all your strength, but the creature is too strong. In the cold grip of the jungle’s embrace, you struggle for breath, the sounds of the night swallowing your cries. The last thing you see is the dense canopy above before everything fades to black."])
                                    wait_for_input()
                                    game_on = handle_death()
                               
                elif path_direction == 'Right':
                    display_text(["As you continue along the right path, the sound of rushing water grows louder. The thick foliage gives way to a breathtaking sight—a majestic waterfall cascading down from towering cliffs, spilling into a crystal-clear pool below. The water sparkles in the sunlight, and the scene feels like a hidden oasis, untouched by time. The mist from the waterfall cools the air around you, providing a welcome relief from the oppressive jungle heat.",
                    "You pause at the edge of the pool, marveling at its beauty. The water shimmers under the sun, catching your eye. Something shiny glimmers beneath the surface—could it be gold? The pool seems peaceful, with no visible dangers."])
                    wait_for_input()
                    
                    pool = None
                    display_text(["Do you choose to:", 
                        "1. Swim in the pool to investigate what's under the water.", 
                        "2. Walk past the pool and keep going."])
                    
                    while pool not in ['Swim', 'Walk']:
                        pool = get_user_choice1(['Swim', 'Walk'])
                        if pool == "Swim":
                            display_text(["You decide to take a chance and dive in. The water is refreshingly cool, and for a moment, the weight of the jungle’s mysteries seems to slip away. You float on your back, gazing up at the sky, enjoying the rare moment of tranquility.",
                            "Suddenly, you feel something brush against your leg. At first, you think it's just a current or a passing fish, but the sensation grows stronger. Before you can react, a powerful force pulls you under the water. You struggle and thrash, but whatever lurks beneath the surface is too strong. Your vision blurs as you're dragged deeper, and the last thing you see is the sunlight fading above as the water pulls you into its cold depths."])
                            wait_for_input()
                            game_on = handle_death()
    
                        elif pool == "Walk":
                            display_text(["The eerie calm of the pool sends a chill down your spine, and you decide to trust your instincts. You skirt around the edge of the water, keeping a safe distance from the inviting but unsettling depths. As you reach the far side of the clearing, you notice something strange.",
                            "Behind the waterfall, partially hidden by the cascading water, is the outline of a cave entrance. The rocks around the entrance are slick with moss, but the passage looks wide enough to walk through. You cautiously approach, realizing that this hidden cave could hold answers—or further dangers.",
                            "With the roar of the waterfall behind you, you take a deep breath and step into the cave’s shadowy entrance. The temperature drops as you leave the warmth of the jungle and enter the cool, damp air of the cave. The sound of rushing water fades, replaced by the quiet drip of moisture from the ceiling. The light filtering in from the waterfall behind you quickly dims as you venture deeper.",
                            "The walls of the cave are slick with moss, and your footsteps echo softly as you walk. After a short distance, the tunnel widens into a larger chamber. Strange markings cover the walls—symbols and carvings that look ancient, but their meaning is unclear. A faint glow illuminates the chamber, coming from an unknown source deeper within the cave.",
                            "As you continue forward, you reach a fork in the path. Two passages branch off in different directions, each leading deeper into the cave. The glow seems to come from both paths, but you can’t tell where they lead. Standing at the crossroads, you feel the weight of the decision pressing down on you."])
                            wait_for_input()
                            
                    cave_passage = None
                    display_text(["Do you choose to:", 
                        "1. Take the left passage, where you hear a faint but rhythmic sound, almost like the beating of drums.", 
                        "2. Take the right passage, where the air feels colder and an occasional breeze flows through, carrying a musty, ancient scent."])
        
        
                    while cave_passage not in ['Left', 'Right']:
                        cave_passage = get_user_choice1(['Left', 'Right'])
                        if cave_passage == "Left":
                            display_text(["You choose the left passage, drawn by the rhythmic sound. The steady beat grows louder as you make your way deeper into the cave. It becomes clear that the noise isn’t drums but rather the steady, unsettling thrum of something alive, something enormous. The walls close in slightly, and the air grows more humid, making it harder to breathe.",
                            "After a few minutes, you arrive at a large open space. At the center of the room lies a massive stone altar, surrounded by strange, pulsing vines that seem to writhe of their own accord. The rhythmic noise is coming from the altar itself."])
                            wait_for_input()
                            
                            stone_altar = None
                            display_text(["Do you choose to", 
                                "1. Approach the altar to investigate the source of the sound.",
                                "2. Turn back, realizing the place feels too dangerous."])

                            while stone_altar not in ['Approach', 'Turn']:
                                if stone_altar == "Approach":
                                    display_text(["Your curiosity gets the better of you, and despite the ominous feeling creeping up your spine, you step closer to the altar. The pulsing vines seem to react to your presence, twitching slightly as you approach. The rhythmic noise grows louder, almost deafening, as if the very air is vibrating with some ancient energy.",
                                    "The altar is carved from dark stone, its surface smooth but worn from centuries of age. Strange symbols are etched into its surface, glowing faintly in time with the rhythm. At the center of the altar lies a small, glowing object—a gemstone, radiating with a dull, pulsating light.",
                                    "As your hand hovers above it, the pulsing vines tighten around the altar, as if guarding the treasure. You can feel the power emanating from the gemstone, but touching it feels like a gamble."])
                                    wait_for_input()
                                    
                                    gemstone = None
                                    display_text(["Do you choose to:",
                                        "1. Grab the gemstone, trusting that it may hold the key to something greater.",
                                        "2. Step away from the altar, sensing that whatever power the gemstone holds is dangerous."])

                                    while gemstone not in ['Grab', 'Step']:
                                        gemstone = get_user_choice1(['Grab', 'Step'])
                                        if gemstone == "Grab":
                                            display_text(["Your curiosity gets the better of you, and despite the growing sense of danger, you reach forward, your hand trembling slightly. As your fingers make contact with the gemstone, a jolt of energy surges through your body. The vines tighten around the altar, constricting rapidly like a snake preparing to strike. The rhythmic hum intensifies, now like a warning bell in your ears.",
                                            "Before you can react, the vines lash out, binding your arms and legs, pulling you toward the altar. The gemstone begins to glow brighter, and the air around you thickens. You try to pull away, but the vines tighten further, and you feel your strength draining away. The ground trembles as though the very temple is waking up, angry at your intrusion.",
                                            "The gemstone pulses one final time, and then, everything goes black."])
                                            wait_for_input()
                                            game_on = handle_death()

                                        elif gemstone == "Step":
                                            display_text(["Something about the gemstone feels wrong, like an invitation to a power you don’t understand. With a nervous glance at the pulsating vines, you step back slowly. The hum continues to resonate around you, but you don’t feel the same urgency to reach for the object. The vines, though still restless, seem to lose their intensity as you distance yourself from the altar.",
                                            "You turn away from the altar, but as you do, you hear a loud crack behind you. The ground begins to shake again, and the rhythmic noise picks up once more, as though the entire temple is waking up in fury. The walls of the chamber start to close in, the air becoming thick with dust.",
                                            "You turn to make a run for the exit, but the door slams shut with a violent thud, trapping you in the room. The vines, once restrained, now spring to life, reaching for you, but this time you’re faster.",
                                            "In a desperate bid for survival, you sprint toward another passage that you barely noticed before, hidden in the shadows. The vines lash out, barely missing you as you dive into the dark corridor. You hear the hiss of the temple, the sound of its fury, but you're alive—at least for now.",
                                            "You narrowly escape, but you’ve made a dangerous enemy. The temple will not forget you so easily.",
                                            "After what feels like an eternity of running, the passage opens into a small, dimly lit chamber. You take a moment to catch your breath, the silence in here almost deafening after the chaos of the last few minutes. The walls are adorned with faded murals of ancient beings, some holding weapons, others with eyes that seem to follow your every movement. In the center of the room, an ancient pedestal stands, a single object resting on it: a weathered map, seemingly abandoned and untouched for centuries.",
                                            "You step closer to the pedestal, curiosity outweighing your fear. The map is rolled up, tied with a fraying string, and when you untie it, it reveals a set of locations, marked with strange symbols, and a path that leads deep into the jungle."])
                                            wait_for_input()
                                            
                                            cave_pedestal = None
                                            display_text(["Do you choose to:",
                                                "1. Take the map and follow the trail."
                                                "2. Search for another exit."])

                                            while cave_pedestal not in ['Map', 'Exit']:
                                                cave_pedestal= get_user_choice1(['Map', 'Exit'])
                                                if cave_pedestal == "Map":
                                                    display_text(["You weigh your options carefully. The map in your hand seems to glow faintly, almost beckoning you to follow its trail deeper into the jungle. Despite the nagging feeling that this could be another trap, the promise of treasure—or at least a way out of the temple’s grasp—is too tempting to ignore. You decide to trust the map, even if it means risking everything.",
                                                    "You take a deep breath, tuck the map into your pack, and turn toward the path indicated on the map. The cave walls, once smooth and unyielding, seem to shift as you move deeper into the dark labyrinth. The air becomes thicker, the dampness more oppressive. The sound of dripping water echoes from somewhere in the distance.",
                                                    "You follow the trail for what feels like hours, your footsteps echoing eerily in the silence. The map guides you deeper into the cave system, but something feels wrong. The air grows colder, and the shadows around you stretch unnaturally long. It becomes clear that the path you’re following is too perfect—too carefully laid out. It’s as if the cave itself is pulling you toward something… or someone.",
                                                    "The walls begin to narrow, and the dim light of your torch flickers. You push forward, your pulse quickening, as the oppressive feeling of being watched grows stronger with each step.",
                                                    "Suddenly, the ground beneath your feet gives way. You stumble and barely manage to catch yourself on a thick vine hanging from the cave’s ceiling. The dark abyss yawns below you, and your heart races as you realize that you’ve walked directly into a trap—spikes, sharp as daggers, wait below.",
                                                    "As you scramble to climb back up, the vines above you shake. A soft, almost imperceptible hum fills the air, and you can feel the earth beneath you tremble. The cave is alive—and it’s closing in on you.",
                                                    "You manage to pull yourself up, but the path you followed now feels like a maze. The walls seem to shift with every step, closing in tighter around you. The map that once seemed to guide you now feels like a cruel joke, leading you deeper into the cave’s heart.",
                                                    "You turn back, hoping to retrace your steps, but the vines seem to have a life of their own. They grow and twist, blocking your path and forcing you further into the heart of the cave. Panic sets in as you realize you’re trapped in the very place you thought would lead you to freedom.",
                                                    "You stumble upon an ancient stone structure, its eerie markings matching those on the map. It looks like a possible exit, but as you step closer, the ground shakes violently. The walls of the cave begin to close in on you. A heavy stone door crashes down behind you, sealing you inside the chamber.",
                                                    "The air grows thick with dust, and the walls seem to close in tighter with each passing second. The shadows grow longer, and you can feel an ominous presence lurking in the darkness. The map has led you here, but now, in the heart of the cave, you realize there is no escape.",
                                                    "There is no treasure. There is no way out. Only death awaits."])
                                                    wait_for_input()
                                                    game_on = handle_death()

                                                elif cave_pedestal == "Exit":
                                                    display_text(["You take a step back from the pedestal, the map forgotten in your hands. Your instincts scream at you to get out of this cursed place before it’s too late. The very air around you feels thick with malice, and every shadow seems to move with an intent of its own. You can’t shake the sense that the temple is closing in on you, waiting for you to make a wrong move.",
                                                    "You decide to search the chamber for an exit, hoping that some hidden doorway will present itself, some way out of this madness.",
                                                    "The chamber is eerily quiet now, but your footsteps echo loudly against the stone. You move along the walls, your fingers tracing the ancient carvings as you look for any sign of a hidden passage. The murals on the walls seem to shift in the flickering light, their eyes following your every move. Sweat beads on your forehead as you push aside the feeling that you’re being watched.",
                                                    "You reach the far corner of the room and notice something strange—a loose stone in the floor. You press on it, and it shifts slightly, revealing a small gap beneath the surface. Your heart races as you kneel down and start pulling away the stone.",
                                                    "As soon as the stone moves, a low rumble fills the room. The ground beneath you begins to tremble, and the walls seem to close in, grinding against each other with a deafening roar. Panic surges through you as the gap you uncovered widens into a deep pit.",
                                                    "You try to scramble away, but the floor beneath your feet gives way. The chamber shakes violently as the trap activates, and the walls begin to collapse inward, sealing off any hope of escape. The last thing you hear is the sound of rushing stone and the slow, inevitable fall into the darkness below."])
                                                    wait_for_input()
                                                    game_on = handle_death()
                                
                                elif stone_altar == "Turn":
                                    display_text(["You decide that the risk isn’t worth it. As you step away from the altar, the vines seem to pulse with a more frantic rhythm, almost as if sensing your retreat. The low growl in the distance grows louder, more threatening, echoing off the walls and vibrating through the floor beneath your feet.",
                                    "You quicken your pace, trying to make your way back to the fork in the path. But the tunnel behind you grows darker, and the ground feels different—less solid, more like something is shifting beneath the surface.",
                                    "Suddenly, the walls begin to close in, but not in the way you expected. The very stone seems to warp and twist, turning the passage into a living maze. The vines that had been harmless before now spring to life, slithering toward you with alarming speed. Before you can react, they wrap around your ankles, tightening with a strength you hadn’t anticipated.",
                                    "You try to run, but the vines pull you back, tightening around your legs, then your torso, constricting like a serpent. Panic surges as you struggle, but the more you fight, the tighter they coil. The growl turns into a guttural roar, and from the darkness, something large and unseen moves toward you.",
                                    "In one final, crushing moment, the vines drag you toward the altar. The last thing you hear is the rhythmic pulsing turning into a deafening thrum before the vines pull you under the ground, the stone swallowing you whole."])
                                    wait_for_input()
                                    game_on = handle_death()

                        elif cave_passage == "Right":
                            display_text(["You take the right passage, following the cool breeze. The air smells musty, but it feels fresher than the other path. The tunnel narrows as you descend, and you have to duck to avoid hitting your head on the low ceiling.",
                            "After a while, the passage opens into a hidden underground lake. The water here is still, almost unnaturally so, and a faint light emanates from the surface. Across the lake, you see what looks like an ancient stone door embedded into the cave wall. The door is covered in intricate carvings, and you sense that something important lies beyond it."])
                            wait_for_input()
                              
                            cave_pool = None
                            display_text(["Do you choose to:", 
                                "1. Swim across the lake to reach the stone door.",
                                "2. Search the edge of the lake for another way around."])
                                
                            while cave_pool not in ['Swim', 'Search']:
                                get_user_choice1(['Swim', 'Search'])
                                if cave_pool == "Swim":
                                    display_text(["You decide to swim across the lake, determined to reach the stone door. The water is cool and refreshing as you dive in, but it quickly becomes apparent that there’s something off about it. The faint light emanates from the water’s surface, but as you swim deeper, the glow becomes more intense, almost blinding.",
                                    "Suddenly, you feel something brush against your leg—something cold and slippery. Panic rises in your chest as you kick harder, swimming faster. But the water begins to pull you down, the current increasing rapidly. No matter how hard you try to swim against it, you feel yourself being dragged under.",
                                    "But you refuse to give up. Summoning every ounce of strength, you push forward. The light ahead grows brighter, guiding you toward the stone door. With one final, powerful stroke, you surge through the water and reach the door. You pull yourself out of the lake, breathless but victorious.",
                                    "The door creaks open with a low rumble, revealing a dark, ancient passageway beyond. You’ve made it.",
                                    "You step through the stone door, your heart still racing from the perilous swim. The passageway beyond is narrow and winding, the walls covered in ancient carvings and symbols. The air is thick with dust and age, but the faint glow of the water's light seems to have followed you, casting an eerie illumination on the path ahead.",
                                    "As you move deeper into the passage, the sound of rushing water fades behind you, replaced by an unsettling silence. The temperature drops, and you begin to notice that the stone walls are slick with moisture, as if the cave itself is alive and breathing. You can feel the weight of the temple pressing in around you, its dark secrets just beyond reach.",
                                    "Suddenly, the corridor widens into a grand chamber. At its center stands a pedestal, upon which rests a large, intricately designed artifact—something that looks like a crown, but unlike any crown you've seen before. It's made of some dark, shimmering metal, and its edges are adorned with glowing gemstones that pulse in rhythm with your heartbeat."])
                                    wait_for_input()
                                    
                                    glowing_gemstone = None
                                    display_text(["Do you choose to:", 
                                        "1. Approach the pedestal and claim the artifact.",
                                        "2. Examine the room for traps."])

                                    while glowing_gemstone not in ['Artifact', 'Traps']:
                                        glowing_gemstone = get_user_choice1(['Artifacts', 'Traps'])
                                        if glowing_gemstone == "Artifact":
                                            display_text(["You feel an overwhelming pull toward the artifact, a deep compulsion that seems to echo within your very soul. The crown’s gleaming gemstones call to you, their rhythm matching the beat of your heart as if they were made for you alone.",
                                            "You step forward, cautiously at first, the weight of every choice you’ve made up to this point heavy on your shoulders. But the allure of the crown is too great. You move closer, reaching out to claim it.",
                                            "As your fingers graze the cold surface of the crown, the room suddenly shifts. The floor trembles beneath you, and a deep rumbling sound fills the air. The gemstones on the crown glow brighter, and the temperature plummets. The once silent chamber now hums with an ominous energy.",
                                            "Before you can react, the pedestal beneath the crown begins to sink into the ground, and the walls start to close in. The passageway behind you is sealed shut with an ancient, stone door that slams down with a deafening noise.",
                                            "You try to move, but the crown begins to radiate an oppressive force, locking you in place. The walls around you shift, their stone faces contorting into grotesque figures as they start to creep toward you, each step accompanied by the deepening hum of the temple.",
                                            "It’s as if the temple itself is alive, and your actions have triggered something ancient and malevolent. The glowing gemstones on the crown pulse faster and faster, like a heartbeat that has quickened with the rise of your doom.",
                                            "A deep, guttural voice echoes from the walls, vibrating the very air. 'Fool. You have awakened that which should remain forgotten.'",
                                            "The walls close in faster now, and the weight of the temple presses down on you. Desperately, you try to break free, but the power of the crown holds you in place. The hum grows deafening, and the temple’s fury surges like an unstoppable force.",
                                            "With one final, crushing surge, the walls engulf you. The darkness closes in, and the last thing you hear is the low hum of the temple… and the soft, haunting rhythm of your own heartbeat, now lost in the depths of the earth."])
                                            wait_for_input()
                                            game_on = handle_death()

                                        elif glowing_gemstone == "Traps":
                                            display_text(["You decide to proceed with caution. The weight of the decision presses on you, and despite the urgency of claiming the artifact, you cannot shake the feeling that something is wrong. You carefully examine the floor, the walls, and the ceiling, searching for any signs of traps.",
                                            "The light from the crown above flickers eerily, casting long shadows across the room. Every step you take feels more deliberate, more calculated. As you scan the area, your eyes fall on a faint, almost invisible line etched into the stone floor near the pedestal. It’s barely noticeable, but it seems to form a hidden tripwire.",
                                            "You kneel down, inspecting it more closely. You can tell that disturbing the wire would trigger something—perhaps spikes from the walls, or a falling ceiling. You carefully bypass the line, stepping over it without disturbing the mechanism. As you proceed, you find another faint marking along the walls—a small panel that can be pressed without triggering any alarm.",
                                            "With a steady hand, you press the panel. A low rumble fills the air, and you brace yourself for whatever may come. But instead of a deadly trap, the stone wall before you slides open, revealing a hidden compartment. Inside, gleaming in the dim light, you find an ancient chest, its wood covered in moss and age, but the lock seems intact.",
                                            "Your heart races as you approach the chest, the sense of danger lifting. You carefully open it, revealing its contents. Inside lies a collection of gold coins, priceless jewels, and, nestled at the bottom, a small but exquisitely crafted dagger with an intricate hilt. The dagger's blade gleams, untouched by time, and you feel an odd sense of power emanating from it.",
                                            "This is the treasure you were seeking—a long-lost relic from the ancient city of Eldor. The chest is filled with artifacts unlike anything you've ever seen: intricately carved statues, rare gemstones, and golden trinkets that shimmer with an ethereal glow. But at the center of it all lies the object of your quest—the Jewel of Endor, a radiant gemstone said to hold immense power. Its light pulses gently, as if it has a heartbeat of its own.",
                                            "You carefully lift the jewel, feeling a surge of energy flow through your fingers. The moment you touch it, the temple seems to react—the air grows warmer, and the hum of the chamber intensifies. It’s as if the very walls of the temple are alive, sensing the power now in your possession.",
                                            "For a moment, you're paralyzed, caught between awe and fear. The treasure of Eldor is more than you ever imagined. But with it comes a warning, an unspoken truth: this artifact is no mere trinket—it holds the key to untold mysteries and dangers, and now that you have it, you are bound to the ancient forces it controls.",
                                            "The ground beneath your feet trembles, and a voice echoes from the depths of the temple, ancient and powerful. 'The path you walk is no longer yours alone,' it whispers. 'The treasure of Endor chooses its bearer. What will you do with the power it grants?'",
                                            "With the Jewel of Eldor in your possession, you stand at a crossroads. Will you use its power for your own gain, or will you protect it from those who seek to exploit its magic? The choice is yours, but know this: The treasure of Endor is not easily forgotten, and those who seek it will come for you."])
                                            wait_for_input()
                                            game_on = handle_win()

                                elif cave_pool == "Search":
                                    display_text(["You decide to search the edge of the lake for another way around. As you step along the shore, the stillness of the water unnerves you. You trace your fingers along the cave walls, hoping to find a hidden path, but all you find are slick, wet rocks.",
                                    "The light from the water seems to grow more intense, and you feel an unnatural pressure building in the air. Suddenly, you hear a soft whisper, and before you can react, the ground beneath your feet crumbles away. The rocks give way, and you fall into a hidden pit, your body crashing into the jagged stone below.",
                                    "Pain shoots through your body as you lose consciousness, and the last thing you hear is the sound of water rising around you, sealing your fate."])
                                    wait_for_input()
                                    game_on = handle_death()

        elif first_choice == 'Camp':
            display_text(["You decide to set up camp for the night, the sounds of the jungle growing quieter as darkness falls. You build a small fire and huddle near it for warmth, trying to settle your nerves. The oppressive heat of the jungle has started to cool, but there’s an unsettling stillness in the air. The forest, usually alive with the sounds of wildlife, seems eerily silent tonight.",
            "The fire crackles, and you begin to feel the pull of exhaustion. Just as your eyes grow heavy, a strange rustling sound interrupts your thoughts. It's too quiet—too deliberate. You sit up, alert, scanning the dark jungle around you.",
            "Suddenly, the ground beneath you shakes with a low, rumbling growl. The hair on the back of your neck stands up. Something is coming. You hear the unmistakable sound of claws scraping against stone, and a dark shape emerges from the shadows, its glowing eyes locked onto you.",
            "A creature, a monstrous, shadowy figure, emerges from the jungle. Its form is jagged, like a twisted version of the temple’s architecture, its body covered in spiny, hardened scales that reflect the faint light from your fire. Its growl vibrates in your chest as it steps closer, its teeth bared in a hungry grin.",
            "You scramble to your feet, heart racing. There’s no time to run—you must fight."])
            wait_for_input()
            
            attack = None
            display_text(["Do you choose to:",
                "1. Grab your weapon and charge the creature head-on.",
                "2. Try to outsmart the creature, using your surroundings to create a trap or distraction.", 
                "3. Throw a burning log from the fire at the creature, hoping to ward it off long enough to escape."])

            while attack not in ['Weapon', 'Outsmart', 'Log']:
                attack = get_user_choice2(['Weapon', 'Outsmart', 'Log'])
                if attack == "Weapon":
                    display_text(["You grab your weapon, a makeshift spear you crafted earlier, and charge the creature with everything you’ve got. Your heart pounds as you aim for the monster’s throat, hoping to pierce its thick hide.",
                    "But as you get closer, the creature moves with incredible speed, its massive claws swiping at you. It knocks the spear from your hands and swipes at your chest, leaving deep gashes. You stumble back, blood staining the ground. Before you can react, it lunges again, tearing into you with savage force.",
                    "Your vision fades as the creature tears you apart, and you realize too late that charging it head-on was a fatal mistake."])
                    wait_for_input()
                    game_on = handle_death()

                elif attack == "Outsmart":
                    display_text(["You take a deep breath, looking around quickly for something to use to your advantage. You spot a large vine hanging from a nearby tree and a few loose rocks. The creature is closing in, but you wait, trying to stay calm.",
                    "You grab a rock and throw it to one side, creating a noise that momentarily distracts the creature. As it turns to investigate, you quickly climb the tree and cut the vine loose. With one swift motion, you swing it toward the creature, lashing it across the face. The creature recoils in pain and confusion, giving you the opening you need.",
                    "It lets out a deafening roar, clearly disoriented, and takes a step back. You seize the moment and grab another rock, hurling it directly at the creature's glowing eyes. It flinches, stunned by the impact, and stumbles backward.",
                    "The creature, growling in frustration, hesitates. It looks like it’s ready to attack again, but the pain and surprise seem to have rattled it. Taking advantage of its momentary weakness, you quickly grab your remaining supplies, ready to fight again if necessary.",
                    "The creature seems to understand that it’s not going to win this battle. With one last snarl, it retreats into the jungle, vanishing into the shadows.",
                    "You stand there for a moment, your heart pounding. The creature is gone—at least for now. You return to your camp, keeping your eyes open for any signs of its return.",
                    "The fire has died down to a smolder, but you’re alive. Exhausted but relieved, you settle down and make yourself as comfortable as possible, though sleep does not come easily. The sounds of the jungle continue around you, but the threat of the creature has subsided.",
                    "With the first rays of sunlight creeping through the trees, you rise from your camp. The air is cool, and the fire has burned low. The creature has not come back, and you’ve survived the night.",
                    "Feeling a surge of determination, you pack up your camp and prepare to continue your journey. The treasure is still ahead, and now nothing feels impossible.",
                    "You head out into the jungle, ready to face whatever challenges lie ahead, knowing that you've already overcome one of the jungle's most dangerous threats. The path forward is uncertain, but you're more prepared than ever to claim the treasure that awaits.",
                    "As you trek through the underbrush, you hear strange noises and feel eyes watching you. Suddenly, you reach a fork in the path."])
                    wait_for_input()
                    
                    path_direction = None
                    display_text(["At the fork, Do you choose to:", 
                        "1. Go left, following a trail of strange footprints.",
                        "2. Go right, where the path seems clearer but leads deeper into the jungle."])

                    while path_direction not in ['Left', 'Right']:
                        path_direction = get_user_choice1(['Left', 'Right'])
                
                        if path_direction == 'Left':
                            display_text(["The footprints lead you to an abandoned temple. Its doors are ajar, and you feel a strong sense of curiosity."])
                            wait_for_input()
                        
                            temple = None
                            display_text(["Do you choose to:", 
                                "1. Enter the temple.",
                                "2. Ignore the temple and keep following the footprints."])
                        
                            while temple not in ['Enter', 'Ignore']:
                                temple = get_user_choice1(['Enter', 'Ignore'])
                            
                                if temple == 'Enter':
                                    display_text(["You step cautiously into the abandoned temple. The air inside is thick with dust, and the dim light from the outside fades as you move deeper into the shadowy structure. The walls are lined with strange, faded murals depicting long-forgotten kings. You feel an ominous presence, as if the temple itself is watching your every move.",
                                    "Suddenly, you hear the grinding sound of stone shifting behind you—the entrance has sealed shut. You're trapped inside.",
                                    "The path ahead leads you into a vast chamber with intricate carvings on the walls, depicting scenes of treasure hunters, ancient kings, and valuable artifacts. The air is thick with dust, and a sense of mystery fills the room. In the center, there’s a stone pedestal with a golden idol atop it. Surrounding the pedestal are several tiles, each marked with different symbols. The plaque on the wall reads:",
                                    "Only the worthy may pass and claim the treasure. Choose wisely, or face the deadly consequences of greed.",
                                    "You examine the symbols on the tiles closely. They seem to correspond to various valuable treasures that could be hidden within the temple. Each tile may lead you closer to the prize—or lead to danger."])
                                    wait_for_input()
                                    
                                    temple_puzzle = None
                                    display_text(["Do you choose to:", 
                                    "1. Step on the tile marked with the symbol of a radiant gem.", 
                                    "2. Step on the tile marked with the symbol of an ancient chest.",
                                    "3. Step on the tile marked with the symbol of a golden crown."])
                            
                                    while temple_puzzle not in ["Gem","Chest", "Crown"]:
                                        temple_puzzle = get_user_choice2(['Gem', 'Chest', 'Crown'])
                                
                                        if temple_puzzle == 'Gem':
                                            display_text(["You step onto the tile with the gem symbol, believing it to represent wealth and fortune. For a moment, the room stays still. Then, the floor beneath you begins to tremble, and the walls start to close in, slowly crushing the room from both sides."])
                                            wait_for_input()
                                            
                                            room_choice = None
                                            display_text(["Do you choose to:",
                                                "1. Run back and choose another tile.",
                                                "2. Look for a hidden lever or switch in the walls."])
                                            
                                            while room_choice not in['Tile', 'Switch']:
                                                room_choice = get_user_choice1(['Tile', 'Switch'])
                                            
                                                if room_choice == 'Tile':
                                                    display_text(["You quickly jump off the tile, hoping to avoid the trap. But the walls continue to close in, inching closer until the room offers no escape. You scramble for a way out, but it’s too late—the walls close in completely, and you are crushed."])
                                                    game_on = handle_death()
                                
                                                elif room_choice == 'Switch':
                                                    display_text(["You search the room frantically and discover a hidden indentation in the wall. Pressing it opens a secret door, leading you to a narrow, dark corridor and escaping the room that was closing in on you.",
                                                    "In the corridor, the path twists and turns, eventually leading to a massive stone door covered in intricate carvings. The door bears a riddle, which must be solved to proceed.",
                                                    "'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'"])
                                                    wait_for_input()
                                                    
                                                    corridor = None
                                                    display_text(["Do you choose to:",
                                                        "1. Stop and answer the riddle.",
                                                        "2. Search the corridor for more clues."])

                                                    while corridor not in ['Riddle', 'Search', 'Force']:
                                                        corridor = get_user_choice2(['Riddle', 'Search'])
                                                
                                                        if corridor == 'Riddle':
                                                            display_text(["You confidently answer the riddle: 'an echo.' The glowing runes flare brightly, and the door begins to grind open.",
                                                            "But as the door creaks ajar, the carvings spring to life. Stone serpents emerge, their fangs glistening like shards of obsidian.",
                                                            "Your answer has triggered a deadly trap—an ancient safeguard designed to punish intruders who rely on wit alone.",
                                                            "The serpents strike, their stone fangs sinking into your body as darkness consumes you.",])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                                    
                                                        elif corridor == 'Search':
                                                            display_text(["You decide to explore the corridor, ignoring the riddle for now. As you search, you notice faint markings on the wall, almost hidden in the dim light.",
                                                            "The markings form a pattern, leading to a loose stone near the floor. Pressing it reveals a hidden compartment containing a small, ancient artifact.",
                                                            "When you place the artifact into a slot on the massive stone door, the glowing runes fade, and the door silently swings open.",
                                                            "Inside, you find a hidden chamber filled with piles of gold, glittering jewels, and ancient artifacts. The Lost Treasure of Eldor lies before you, untouched for centuries.",
                                                            "Your cleverness and caution have rewarded you with the treasure. You take it home and celebrate your victory."])
                                                            wait_for_input()
                                                            game_on = handle_win()
                                                            
                                                        elif corridor == 'Force':
                                                            display_text([
                                                            "You attempt to force the door open with brute strength. The glowing runes flicker violently, and the carvings seem to shift, reacting to your defiance.",
                                                            "Suddenly, the ground beneath you trembles, and the walls close in. A crushing noise fills the air as the ancient mechanisms spring to life.",
                                                            "Your reckless actions have triggered the corridor's fail-safe. You are crushed as the walls seal shut, ending your adventure.",
                                                            "You have died."])
                                                            wait_for_input()
                                                            game_on = handle_death()

                                        elif temple_puzzle == 'Chest':
                                            display_text(["You cautiously step onto the tile with the chest symbol. The room shakes slightly, but nothing seems to happen. After a moment, the pedestal in the center of the room glows faintly, and the lid of the chest opens, revealing a treasure map inside. It's partially torn, but you can make out markings that could lead to the Lost Treasure of Eldor."])
                                            temple_chest = None
                                            display_text(["Do you choose to:", 
                                                "1. Quickly take the treasure map.",
                                                "2. Examine the chest further."])
                                            
                                            while temple_chest not in ['Take', 'Examine']:
                                                temple_chest = get_user_choice1(['Take', 'Examine'])
                                                if temple_chest == 'Take':
                                                    display_text(["The moment you touch the map, the room shudders, and a trapdoor opens beneath your feet. You fall to your death into a dark pit below with spikes sticking up."])
                                                    wait_for_input()
                                                    game_on = handle_death()
                                
                                                elif temple_chest == 'Examine':
                                                    display_text(["You open the chest completely and discover a hidden compartment beneath the false bottom. Inside, you find a golden artifact—perhaps a key or symbol related to the treasure’s final location. With the artifact in hand, you begin to look around the room for a way out. As you approach the pedestal, you notice a strange indentation in the stone directly beneath it—a keyhole. You realize that the artifact may fit into this keyhole, but the consequences of doing so are unclear. The artifact seems to pulse with energy, almost as if it's urging you forward.",
                                                    "You place the artifact into the keyhole, and as it clicks into place, the ground shakes. A deep rumbling echoes throughout the chamber as the walls begin to move, opening a door leading down a corridor.",
                                                    "You brace yourself as you continue forward. As you go down the corridor, you enter a room with two passages. The first passage is a gleaming golden passage with lots of light and everything made of gold, leading upward. The second passage is a dark, shadowy passage leading downward, where eerie whispers can be heard.",
                                                    "The artifact pulses again, as if signaling that only one path will lead to the treasure, while the other may lead to your doom."])
                                                    wait_for_input()
                                                        
                                                    temple_passageway = None
                                                    display_text(["Do you choose to:",
                                                        "1. Choose the golden passage."
                                                        "2. Choose the shadowy passage."])

                                                    while temple_passageway not in ['Golden', 'Shadowy']:
                                                        temple_passageway= get_user_choice1(['Golden', 'Shadowy'])
                                                            
                                                        if temple_passageway == 'Golden':
                                                            display_text(["You step carefully onto the golden path, your heart racing with excitement. But as you move forward, the walls begin to close in once again. The ground beneath you trembles, and the golden path seems to shift and distort. It's a trap!",
                                                            "A massive stone block drops from above, trapping you in place. You struggle, but it’s too late—the crushing weight of the block sends you plummeting into darkness."])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                                            

                                                        elif temple_passageway == 'Shadowy':
                                                            display_text(["You take a deep breath and step into the shadowy passage. The eerie whispers grow louder, but you press on. The path twists, and soon you find yourself standing before another door—a massive stone door with intricate markings and a single keyhole in the center.",
                                                            "You insert the golden artifact into the keyhole. With a loud click, the door creaks open, revealing a hidden chamber. And there it is, gleaming in the dim light—the Lost Treasure of Eldor."])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                    
                                        elif temple_puzzle == 'Crown':
                                            display_text(["You step onto the tile with the crown symbol, thinking it represents leadership and the rule of a powerful king. The floor seems stable for a moment, but then you hear a faint clicking noise. A set of spikes begins to emerge from the walls, aiming directly at you."])
                                            wait_for_input()
                                            
                                            temple_crown = None
                                            display_text(["Do you choose to:", 
                                                "1. Dodge the spikes and step off the tile.",
                                                "2. Try to find a way to disarm the trap."])
                                            
                                            while temple_crown not in ['Dodge', 'Disarm']:
                                                temple_crown = get_user_choice1(['Dodge', 'Disarm'])
                                                
                                                if temple_crown == 'Dodge':
                                                    display_text(["With a burst of adrenaline, you leap to the side just in time, narrowly avoiding the deadly spikes that shoot from the walls. The hiss of metal scraping against stone echoes in your ears as you land hard, breathless but alive. The crown tile remains glowing ominously, the spikes retracting back into their hidden slots as if waiting for another misstep.",
                                                    "You wipe the sweat from your brow, heart still pounding. You know now that every move must be precise if you’re to survive this ancient temple.",
                                                    "You step back, feeling the weight of the temple's ancient tricks and traps closing in on you. The air is heavy with dust, and you realize that relying solely on the floor tiles may not be the wisest strategy. The temple is a puzzle in itself, and its secrets may be lurking elsewhere—above, below, or around you.",
                                                    "You stop, your eyes scanning the room. Perhaps there's more to this chamber than meets the eye.",
                                                    "As you look around the room you see 3 potential paths you could try or could they be 3 potential traps."])
                                                    wait_for_input()
                                                       
                                                    three_paths = None
                                                    display_text(["Your 3 potential paths are:",
                                                    "1. Search the walls.",
                                                    "2. Examine the ceiling.",
                                                    "3. Look for a hidden passage in the corners of the room."])
                                                    
                                                    while three_paths not in ['Walls', 'Ceiling', 'Corners']:
                                                        three_paths = get_user_choice2   
                                                        
                                                        if three_paths == "Walls":
                                                            display_text(["You run your hands along the cold stone walls, feeling for any unusual bumps or cracks. As you press on different sections, one stone shifts slightly under your fingers. It feels loose, as if it were designed to move."])
                                                            wait_for_input()
                                                            
                                                            temple_stone = None
                                                            display_text(["Do you choose to:", 
                                                            "1. Press the loose stone further and see if it triggers something.",
                                                            "2. Leave it alone and explore another part of the wall."])
                                                            
                                                            while temple_stone not in ['Press', 'Leave']:
                                                                temple_stone = get_user_choice1  
                                                                if temple_stone == "Press":
                                                                    display_text(["Cautiously, you press the stone deeper into the wall. At first, nothing happens, but then you hear a soft click. A sudden chill runs down your spine. Before you can react, steel clamps snap around your wrist, trapping your hand against the wall.",
                                                                    "A hiss fills the air—cold, sharp, and ominous. You glance up in horror as small nozzles emerge from the wall above the stone, releasing a faint mist. Your heart pounds as the acrid smell of toxic gas hits your nostrils.",
                                                                    "You try to pull your hand free, but the clamp holds tight. Panic surges through you as your vision starts to blur, and a burning sensation spreads through your lungs. The gas is taking effect—there's no escape.",
                                                                    "As your strength fades, you realize this was a trap meant to keep treasure seekers like you from proceeding. Your hand remains pinned, and the gas consumes you."])
                                                                    wait_for_input()
                                                                    game_on = handle_death()
                                                                
                                                                elif temple_stone == "Leave":
                                                                    display_text(["Something in your gut tells you not to press your luck. You step back, deciding that the stone might not hold the solution you need. Instead, you continue along the wall, carefully feeling for any other clues or mechanisms.",
                                                                    "In the far corner, you find a barely perceptible seam—a crack in the wall that seems too deliberate to be a natural flaw. Pushing gently, a section of the wall slides away, revealing a narrow hidden passage.",
                                                                    "The passage narrows as you move forward, the air thick with dust and the scent of long-forgotten secrets. Your footsteps echo off the stone walls, growing louder in the oppressive silence. After what feels like an eternity, you arrive at the end of the passage—a large, ornate chamber with high ceilings and walls adorned with faded murals of ancient treasure hunters.",
                                                                    "At the center of the room stands an elaborate stone altar, covered in intricate carvings. On top of the altar lies a weathered chest, its edges chipped and covered in ancient moss. To the left, a large stone door blocks your exit.",
                                                                    "A faint humming sound fills the air, and your eyes are drawn to the strange glow coming from the chest. You approach, hesitant but determined. On the stone door, an inscription catches your eye:",
                                                                    "Where shadows dwell, the light will reveal what’s hidden. Only those who seek with more than their eyes may find it.",
                                                                    "The room is eerily still, and there's an unsettling sense that something is watching you. You realize the inscription could be the key, but it doesn’t make sense right away."])
                                                                    wait_for_input()
                                                                    
                                                                temple_clue = None
                                                                display_text(["Do you choose to:", 
                                                                "1. Look around the room for a hidden light source or another clue.",
                                                                "2. Open the chest without further investigation."])
                                                            
                                                                while temple_clue not in ['Look', 'Open']:
                                                                    temple_clue = get_user_choice1(['Look', 'Open'])
                                                            
                                                                    if temple_clue == "Look":
                                                                        display_text(["You step back from the chest, the inscription repeating in your mind: 'Where shadows dwell, the light will reveal what’s hidden.' You scan the room, looking for any unusual features.",
                                                                        "The walls are covered in faded murals, but one near the far side of the chamber catches your attention. It depicts a scene of an ancient explorer entering a treasure room, and in the shadows of the artwork, there’s a faint glimmer of light.",
                                                                        "You step toward the mural and notice something odd about the area where the light seems to be coming from—it’s not a painting at all. Instead, it's a small indentation in the stone wall, cleverly disguised. You press it gently, and a faint click echoes through the chamber.",
                                                                        "Suddenly, a beam of light shoots out from the wall, illuminating the room. The chest you were about to open is now bathed in the glow, but something else catches your eye—the floor beneath the chest shifts, revealing a hidden compartment carved into the stone slab.",
                                                                        "Kneeling down, you carefully lift the lid of the compartment and find an ancient key—its intricate design matching the carvings on the walls. Next to the key lies a note, fragile with age, but still legible:",
                                                                        "'The final key to the treasure lies beyond this room, where light and shadow meet. Use this key, and the path shall be revealed.'",
                                                                        "You turn back toward the chamber, the key in hand, when you notice a small keyhole embedded in one of the nearby pillars. The carvings around the keyhole match the designs on the key perfectly. With trembling hands, you insert the key and turn it slowly.",
                                                                        "Click.",
                                                                        "The ground shakes for a moment, and then the wall in front of you begins to shift. Stones slide aside, revealing a narrow passage that glows with a golden hue. You can hardly believe it, but as you step inside, the passage opens into a magnificent chamber.",
                                                                        "The treasure is here. Piles of gold, gleaming jewels, and ancient artifacts are scattered across the room, undisturbed for centuries. At the center, a golden idol, encrusted with gemstones, sits on a raised platform—the heart of the treasure you've sought for so long."])
                                                                        wait_for_input()
                                                                        game_on = handle_win()
                                                                    
                                                                    elif temple_clue == "Open":
                                                                        display_text(["You decide to ignore the inscription and open the chest, eager for the treasure inside. As you lift the lid, you hear a click, and the chest immediately begins to shake violently.",
                                                                        "Before you can react, a cloud of noxious green gas billows out of the chest, filling the air around you. You stagger backward, coughing, trying to wave the gas away, but it's no use. Your vision blurs, and the room seems to spin.",
                                                                        "Suddenly, something moves in the shadows near the chest. You blink, trying to focus, but it's too late. A large, snake-like creature slithers out from the chest, its scales glistening in the dim light. Its eyes glow with an eerie, predatory light, and with a swift, deadly strike, it lunges toward you.",
                                                                        "You try to dodge, but the gas has weakened your movements. The creature's fangs sink into your leg, and a burning sensation spreads through your body. You collapse to the ground, the world fading as the poison takes hold.",
                                                                        "The chest was a trap, and now the treasure, whatever it may be, is lost to you forever."])
                                                                        wait_for_input()
                                                                        game_on = handle_death()
                                    
                                                        elif three_paths == "Ceiling":
                                                            display_text(["You tilt your head up, squinting at the ceiling. Among the cracks and worn stone, you notice faint carvings—symbols that resemble those on the tiles below. Could they be connected? As you study them, you realize the patterns are inverted versions of the floor tiles.",
                                                            "Following the ceiling's guide, you step onto the mirrored tile. As you press down, a soft click echoes through the chamber. The tile glows faintly, and the door across the room slowly creaks open, revealing a hidden passage. You smile, realizing you've cracked the temple's puzzle and can now move deeper into the treasure vault.",
                                                            "You step cautiously toward the newly revealed passage. The air inside the corridor is cooler and damp with the scent of ancient stone. The dim light from the chamber behind you fades as you venture further into the tunnel. Your heart races, feeling like you're getting very close to the treasure.",
                                                            "As you move deeper, the passage widens into a vast underground chamber. The walls are lined with towering stone columns, each carved with intricate depictions of explorers, treasure, and mysterious symbols. In the center of the chamber stands a massive stone pedestal, and atop it, a golden chest gleams in the flickering torchlight.",
                                                            "But something feels off. The floor between you and the chest is covered with more tiles, each inscribed with different symbols—many of which match the ones you've seen before. A faint draft whispers through the chamber, and you can’t shake the feeling that another trap is waiting."])
                                                            wait_for_input()
                                                            
                                                            no_way_out = None
                                                            display_text(["Do you choose to:", 
                                                            "1. Carefully inspect the floor for traps.",
                                                            "2. Walk directly to the chest, confident you've solved the temple's riddles.",
                                                            "3. Search the chamber for hidden clues or switches."])
                                                            
                                                            while no_way_out not in ['Inspect', 'Walk', 'Look']:
                                                                no_way_out = get_user_choice2(['Inspect', 'Walk', 'Look'])
                                                                
                                                                if no_way_out == "Inspect":
                                                                    display_text(["You crouch and carefully examine each tile. You notice subtle differences—the edges of certain tiles are slightly raised, and others seem worn from centuries of use. You deduce that the raised tiles are pressure-sensitive traps. Slowly, you step only on the worn, safer tiles.",
                                                                    "But just as you near the chest, your foot presses down ever so slightly on an unnoticed raised tile. A split second later, sharp darts shoot out from the walls, striking you in the back before you can react. You collapse to the ground, your vision blurring as the chamber spins."])
                                                                    wait_for_input()
                                                                    game_on = handle_death()
                                                                
                                                                elif no_way_out == "Walk":
                                                                    display_text(["You march confidently across the room, certain that you’ve solved all of the temple’s riddles. The chest is right in front of you, waiting to be opened. But just as your hand touches the lid, a soft click sounds beneath your feet.",
                                                                    "Without warning, a barrage of poisoned darts flies out from hidden holes in the walls, striking you from every direction. You gasp in pain, feeling the toxins work fast. Your vision darkens, and your legs give way as you fall to the floor."])
                                                                    wait_for_input()
                                                                    game_on = handle_death()
                                                    
                                                                elif no_way_out == "Look":
                                                                    display_text(["You decide there must be another way—something hidden in the chamber that can help you safely reach the treasure. After all, these temples are notorious for tricks. You begin to examine the walls and floor, searching for hidden clues or switches.",
                                                                    "As you run your hand along the cold stone, you feel a slight depression in the wall. Without thinking, you press it, triggering a hidden mechanism. Instead of revealing a secret, a volley of poisoned darts bursts from the walls. They hit you all at once, the poison working quickly. You stumble, your body betraying you as you fall to the ground."])
                                                                    wait_for_input()
                                                                    game_on = handle_death()
                                                                    
                                                        elif three_paths == "Corners":
                                                            display_text(["You cautiously approach the key, eyes scanning the floor and walls for any signs of danger. Your instincts tell you to be careful, but the allure of the golden artifact is too strong to resist. As your hand wraps around the cool metal of the key, nothing happens at first.",
                                                            "But then, the moment you lift the key off the pedestal, a deafening click echoes through the room. The walls begin to tremble violently, and the floor shifts beneath your feet. Before you can react, the ceiling starts to lower, revealing a network of small holes along the edges of the walls.",
                                                            "With a hiss, a barrage of poisoned darts shoots out from every corner, raining down on you from all sides. You try to dodge, but the darts are too fast, too many. One after another, they pierce your skin. You feel the burning sting of the poison coursing through your veins.",
                                                            "The ceiling continues to descend slowly, adding to the terror. Your limbs feel heavy, your vision blurs, and within moments, the world fades to black."])
                                                            game_on = handle_death()

                                                elif temple_crown == "Disarm":
                                                    display_text(["You quickly assess the situation, and your instincts scream at you to find a way to stop the trap before the spikes reach you. You frantically search the walls for any hidden levers or panels. Your eyes catch sight of a small, almost imperceptible panel near the edge of the floor, slightly out of view but within reach.",
                                                    "With no time to lose, you lunge toward it, pressing your hand against the stone to reveal the hidden mechanism. A lever appears, and you yank it down with all your strength, hoping to stop the deadly spikes in their tracks.",
                                                    "For a moment, the spikes halt, their deadly points mere inches from you. Your heart races, and you breathe a sigh of relief, thinking you’ve narrowly escaped death. But just as the tension begins to ease, you hear a loud, mechanical whirring sound coming from above.",
                                                    "Too late, you realize that the trap you’ve disarmed wasn’t fully disabled—it triggered an even deadlier secondary mechanism. The ceiling above you begins to lower at an alarming speed, and before you can react, massive stone blocks descend, trapping you in the chamber.",
                                                    "You struggle to escape, but the walls close in too quickly. The pressure of the falling stones crushes you under their weight."])
                                                    wait_for_input()
                                                    game_on = handle_death()

                                elif temple == "Ignore":
                                    display_text(["You decide to ignore the temple’s ominous presence and the dangers lurking within. The footsteps you’ve been following seem like a safer route, so you turn your back on the mysterious structure and press on.",
                                    "As you walk deeper into the jungle, the sound of the footsteps grows clearer, and you start to wonder who—or what—is leaving them. The path is dense with vegetation, and the air grows thicker with humidity. The footsteps continue to echo, drawing you further into the wild.",
                                    "After hours of walking, the footsteps suddenly stop. Just as the sun is going down and it's getting dark, you find yourself standing at the edge of a dark, cavernous opening in the jungle, hidden behind thick vines and overgrown trees. The air here feels colder, and the shadows seem to stretch unnaturally long.",
                                    "You peer inside, but the darkness is almost absolute. The footsteps seem to have disappeared."])
                                    wait_for_input()
                                    
                                    cave = None
                                    display_text(["Do you choose to:", 
                                    "1. Enter the cave.",
                                    "2. Set up camp."])

                                    while cave not in['Enter', 'Set Up']:
                                        cave = get_user_choice1(['Enter', 'Set Up'])
                                        if cave == "Enter":
                                            display_text(["You take a step into the cave, your torch flickering as you descend into the darkness. The walls are covered in glowing moss, and the air smells damp. The further you go, the more oppressive the silence becomes. The footsteps that guided you here have vanished, but you feel a strange compulsion to keep going deeper.",
                                            "After what feels like an eternity, you arrive at a vast underground chamber. It’s filled with ancient ruins—crumbling stone pillars, scattered bones, and an eerie stillness. In the center of the room stands an ornate chest, seemingly untouched by time. The air feels thick with anticipation as you move toward it, your heart racing. Could this be the treasure you've been seeking?",
                                            "As you approach the chest, you notice strange markings carved into the stone floor, surrounding it in a perfect circle. Something about the symbols feels wrong, as though they were meant to keep something in, not out. The chest beckons, its golden trim glinting in the low light."])
                                            wait_for_input()
                                            
                                            cave_choice = None
                                            display_text([
                                                "Do you choose to:", 
                                                "1. Open the chest.",
                                                "2. Examine the markings on the cave floor.",
                                                "3. Leave the cave."])
                                                
                                            if cave_choice == "Open":
                                                display_text(["You place your hands on the chest's heavy lid and push. The moment it opens, a cloud of dust billows into the air, and a low rumbling sound fills the chamber. Before you can react, the walls begin to shake violently, and you hear the sound of metal scraping on stone.",
                                                "Suddenly, the chest seems to collapse in on itself, a horrifying mechanism activated by your touch. The lid slams shut, trapping your hands inside. A sharp pain shoots up your arms as the chest begins to constrict around you.",
                                                "You try to pull away, but it's no use—the chest continues to tighten, and the air in the cave becomes thick with a suffocating fog. The last thing you hear is a low hiss as the mist begins to overwhelm you, choking off your breath. Your vision fades as you lose consciousness, and your body is slowly crushed within the trap."])
                                                wait_for_input()
                                                game_on = handle_death()

                                            elif cave_choice == "Examine":
                                                display_text(["You kneel down to inspect the markings, your fingers tracing the strange symbols etched into the stone. The patterns seem to shift under your touch, and a cold shiver runs down your spine. The symbols are ancient, possibly warning signs to anyone foolish enough to enter this chamber.",
                                                "Suddenly, as your fingers press deeper into one of the symbols, you hear a loud click. The ground beneath you trembles, and you realize too late that you’ve triggered a trap. The floor cracks open around you, and a swarm of sharp spikes shoots up from the ground below.",
                                                "You have no time to react as the spikes impale you from all sides, your body swiftly pierced by their razor tips."])
                                                wait_for_input()
                                                game_on = handle_death()
                                                    
                                        elif cave == 'Set Up':
                                            display_text(["The darkening jungle makes you reconsider your course of action. You can barely see where you're going, and the path ahead seems treacherous. You decide to set up camp for the night, hoping the morning light will give you a better chance at finding the treasure.",
                                            "You gather some dry wood and start a fire, the flames crackling in the growing cold. The shadows around you stretch longer, but you feel a sense of safety as you huddle by the warmth of the fire. The forest seems quieter at night, the wildlife eerily absent.",
                                            "The fire flickers and crackles, casting strange shadows across the jungle. You lie down to sleep, the fire’s warmth slowly lulling you into a sense of security. As you drift into slumber, the jungle around you seems to come alive with distant whispers. The air feels thick and oppressive.",                                       
                                            "Your dreams are filled with strange visions—an ancient chest, a golden amulet, and a hidden treasure far beneath the jungle floor. The treasure is close, but it seems just out of reach, like a fleeting dream. As the night deepens, your dreams grow darker and more frantic.",
                                            "You wake to the sound of rustling in the bushes, but when you sit up, there’s nothing there. The fire has gone out, and the jungle is unnervingly quiet. A sense of dread fills the air. You get up to check your surroundings, but before you can react, a low growl echoes from the darkness.",
                                            "Suddenly, a pair of glowing eyes peer from the underbrush, and you feel a cold shiver crawl down your spine. Before you can draw your weapon or react, the jungle around you bursts to life. A creature, something inhuman, leaps from the shadows and tackles you to the ground.",
                                            "You fight back with all your strength, but the creature is too strong. In the cold grip of the jungle’s embrace, you struggle for breath, the sounds of the night swallowing your cries. The last thing you see is the dense canopy above before everything fades to black."])
                                            wait_for_input()
                                            game_on = handle_death()
                                    
                        elif path_direction == 'Right':
                            display_text(["As you continue along the right path, the sound of rushing water grows louder. The thick foliage gives way to a breathtaking sight—a majestic waterfall cascading down from towering cliffs, spilling into a crystal-clear pool below. The water sparkles in the sunlight, and the scene feels like a hidden oasis, untouched by time. The mist from the waterfall cools the air around you, providing a welcome relief from the oppressive jungle heat.",
                            "You pause at the edge of the pool, marveling at its beauty. The water shimmers under the sun, catching your eye. Something shiny glimmers beneath the surface—could it be gold? The pool seems peaceful, with no visible dangers."])
                            wait_for_input()
                            
                            pool = None
                            display_text(["Do you choose to:", 
                                "1. Swim in the pool to investigate what's under the water.",
                                "2. Walk past the pool and keep going."])
                            
                            while pool not in ['Swim', 'Walk']:
                                pool = get_user_choice1(['Swim', 'Walk'])
                                if pool == "Swim":
                                    display_text(["You decide to take a chance and dive in. The water is refreshingly cool, and for a moment, the weight of the jungle’s mysteries seems to slip away. You float on your back, gazing up at the sky, enjoying the rare moment of tranquility.",
                                    "Suddenly, you feel something brush against your leg. At first, you think it's just a current or a passing fish, but the sensation grows stronger. Before you can react, a powerful force pulls you under the water. You struggle and thrash, but whatever lurks beneath the surface is too strong. Your vision blurs as you're dragged deeper, and the last thing you see is the sunlight fading above as the water pulls you into its cold depths."])
                                    wait_for_input()
                                    game_on = handle_death()
            
                                elif pool == "Walk":
                                    display_text(["The eerie calm of the pool sends a chill down your spine, and you decide to trust your instincts. You skirt around the edge of the water, keeping a safe distance from the inviting but unsettling depths. As you reach the far side of the clearing, you notice something strange.",
                                    "Behind the waterfall, partially hidden by the cascading water, is the outline of a cave entrance. The rocks around the entrance are slick with moss, but the passage looks wide enough to walk through. You cautiously approach, realizing that this hidden cave could hold answers—or further dangers.",
                                    "With the roar of the waterfall behind you, you take a deep breath and step into the cave’s shadowy entrance. The temperature drops as you leave the warmth of the jungle and enter the cool, damp air of the cave. The sound of rushing water fades, replaced by the quiet drip of moisture from the ceiling. The light filtering in from the waterfall behind you quickly dims as you venture deeper.",
                                    "The walls of the cave are slick with moss, and your footsteps echo softly as you walk. After a short distance, the tunnel widens into a larger chamber. Strange markings cover the walls—symbols and carvings that look ancient, but their meaning is unclear. A faint glow illuminates the chamber, coming from an unknown source deeper within the cave.",
                                    "As you continue forward, you reach a fork in the path. Two passages branch off in different directions, each leading deeper into the cave. The glow seems to come from both paths, but you can’t tell where they lead. Standing at the crossroads, you feel the weight of the decision pressing down on you."])
                                    wait_for_input()
                                    
                            cave_passage = None
                            display_text(["Do you choose to:", 
                            "1. Take the left passage, where you hear a faint but rhythmic sound, almost like the beating of drums.",
                            "2. Take the right passage, where the air feels colder and an occasional breeze flows through, carrying a musty, ancient scent."])
                             
                            while cave_passage not in ['Left', 'Right']:
                                cave_passage = get_user_choice1(['Left', 'Right'])
                                if cave_passage == "Left":
                                    display_text(["You choose the left passage, drawn by the rhythmic sound. The steady beat grows louder as you make your way deeper into the cave. It becomes clear that the noise isn’t drums but rather the steady, unsettling thrum of something alive, something enormous. The walls close in slightly, and the air grows more humid, making it harder to breathe.",
                                    "After a few minutes, you arrive at a large open space. At the center of the room lies a massive stone altar, surrounded by strange, pulsing vines that seem to writhe of their own accord. The rhythmic noise is coming from the altar itself."])
                                    wait_for_input()
                                    
                                    stone_altar = None
                                    display_text(["Do you choose to:", 
                                    "1. Approach the altar to investigate the source of the sound.",
                                    "2. Turn back, realizing the place feels too dangerous."])

                                    while stone_altar not in ['Approach', 'Turn']:
                                        if stone_altar == "Approach":
                                            display_text(["Your curiosity gets the better of you, and despite the ominous feeling creeping up your spine, you step closer to the altar. The pulsing vines seem to react to your presence, twitching slightly as you approach. The rhythmic noise grows louder, almost deafening, as if the very air is vibrating with some ancient energy.",
                                            "The altar is carved from dark stone, its surface smooth but worn from centuries of age. Strange symbols are etched into its surface, glowing faintly in time with the rhythm. At the center of the altar lies a small, glowing object—a gemstone, radiating with a dull, pulsating light.",
                                            "As your hand hovers above it, the pulsing vines tighten around the altar, as if guarding the treasure. You can feel the power emanating from the gemstone, but touching it feels like a gamble."])
                                            wait_for_input()
                                            
                                            gemstone = None
                                            display_text(["Do you choose to:",  
                                            "1. Grab the gemstone, trusting that it may hold the key to something greater.",
                                            "2. Step away from the altar, sensing that whatever power the gemstone holds is dangerous."])

                                            while gemstone not in ['Grab', 'Step']:
                                                gemstone = get_user_choice1(['Grab', 'Step'])
                                                if gemstone == "Grab":
                                                    display_text(["Your curiosity gets the better of you, and despite the growing sense of danger, you reach forward, your hand trembling slightly. As your fingers make contact with the gemstone, a jolt of energy surges through your body. The vines tighten around the altar, constricting rapidly like a snake preparing to strike. The rhythmic hum intensifies, now like a warning bell in your ears.",
                                                    "Before you can react, the vines lash out, binding your arms and legs, pulling you toward the altar. The gemstone begins to glow brighter, and the air around you thickens. You try to pull away, but the vines tighten further, and you feel your strength draining away. The ground trembles as though the very temple is waking up, angry at your intrusion.",
                                                    "The gemstone pulses one final time, and then, everything goes black."])
                                                    wait_for_input()
                                                    game_on = handle_death()

                                                elif gemstone == "Step":
                                                    display_text(["Something about the gemstone feels wrong, like an invitation to a power you don’t understand. With a nervous glance at the pulsating vines, you step back slowly. The hum continues to resonate around you, but you don’t feel the same urgency to reach for the object. The vines, though still restless, seem to lose their intensity as you distance yourself from the altar.",
                                                    "You turn away from the altar, but as you do, you hear a loud crack behind you. The ground begins to shake again, and the rhythmic noise picks up once more, as though the entire temple is waking up in fury. The walls of the chamber start to close in, the air becoming thick with dust.",
                                                    "You turn to make a run for the exit, but the door slams shut with a violent thud, trapping you in the room. The vines, once restrained, now spring to life, reaching for you, but this time you’re faster.",
                                                    "In a desperate bid for survival, you sprint toward another passage that you barely noticed before, hidden in the shadows. The vines lash out, barely missing you as you dive into the dark corridor. You hear the hiss of the temple, the sound of its fury, but you're alive—at least for now.",
                                                    "You narrowly escape, but you’ve made a dangerous enemy. The temple will not forget you so easily.",
                                                    "After what feels like an eternity of running, the passage opens into a small, dimly lit chamber. You take a moment to catch your breath, the silence in here almost deafening after the chaos of the last few minutes. The walls are adorned with faded murals of ancient beings, some holding weapons, others with eyes that seem to follow your every movement. In the center of the room, an ancient pedestal stands, a single object resting on it: a weathered map, seemingly abandoned and untouched for centuries.",
                                                    "You step closer to the pedestal, curiosity outweighing your fear. The map is rolled up, tied with a fraying string, and when you untie it, it reveals a set of locations, marked with strange symbols, and a path that leads deep into the jungle."])
                                                    wait_for_input()
                                                    
                                                    cave_pedestal = None
                                                    display_text(["Do you choose to:", 
                                                        "1. Take the map and follow the trail.",
                                                        "2. Search for another exit."])

                                                    while cave_pedestal not in ['Map', 'Exit']:
                                                        cave_pedestal= get_user_choice1(['Map', 'Exit'])
                                                        if cave_pedestal == "Map":
                                                            display_text(["You weigh your options carefully. The map in your hand seems to glow faintly, almost beckoning you to follow its trail deeper into the jungle. Despite the nagging feeling that this could be another trap, the promise of treasure—or at least a way out of the temple’s grasp—is too tempting to ignore. You decide to trust the map, even if it means risking everything.",
                                                            "You take a deep breath, tuck the map into your pack, and turn toward the path indicated on the map. The cave walls, once smooth and unyielding, seem to shift as you move deeper into the dark labyrinth. The air becomes thicker, the dampness more oppressive. The sound of dripping water echoes from somewhere in the distance.",
                                                            "You follow the trail for what feels like hours, your footsteps echoing eerily in the silence. The map guides you deeper into the cave system, but something feels wrong. The air grows colder, and the shadows around you stretch unnaturally long. It becomes clear that the path you’re following is too perfect—too carefully laid out. It’s as if the cave itself is pulling you toward something… or someone.",
                                                            "The walls begin to narrow, and the dim light of your torch flickers. You push forward, your pulse quickening, as the oppressive feeling of being watched grows stronger with each step.",
                                                            "Suddenly, the ground beneath your feet gives way. You stumble and barely manage to catch yourself on a thick vine hanging from the cave’s ceiling. The dark abyss yawns below you, and your heart races as you realize that you’ve walked directly into a trap—spikes, sharp as daggers, wait below.",
                                                            "As you scramble to climb back up, the vines above you shake. A soft, almost imperceptible hum fills the air, and you can feel the earth beneath you tremble. The cave is alive—and it’s closing in on you.",
                                                            "You manage to pull yourself up, but the path you followed now feels like a maze. The walls seem to shift with every step, closing in tighter around you. The map that once seemed to guide you now feels like a cruel joke, leading you deeper into the cave’s heart.",
                                                            "You turn back, hoping to retrace your steps, but the vines seem to have a life of their own. They grow and twist, blocking your path and forcing you further into the heart of the cave. Panic sets in as you realize you’re trapped in the very place you thought would lead you to freedom.",
                                                            "You stumble upon an ancient stone structure, its eerie markings matching those on the map. It looks like a possible exit, but as you step closer, the ground shakes violently. The walls of the cave begin to close in on you. A heavy stone door crashes down behind you, sealing you inside the chamber.",
                                                            "The air grows thick with dust, and the walls seem to close in tighter with each passing second. The shadows grow longer, and you can feel an ominous presence lurking in the darkness. The map has led you here, but now, in the heart of the cave, you realize there is no escape.",
                                                            "There is no treasure. There is no way out. Only death awaits."])
                                                            wait_for_input()
                                                            game_on = handle_death()

                                                        elif cave_pedestal == "Exit":
                                                            display_text(["You take a step back from the pedestal, the map forgotten in your hands. Your instincts scream at you to get out of this cursed place before it’s too late. The very air around you feels thick with malice, and every shadow seems to move with an intent of its own. You can’t shake the sense that the temple is closing in on you, waiting for you to make a wrong move.",
                                                            "You decide to search the chamber for an exit, hoping that some hidden doorway will present itself, some way out of this madness.",
                                                            "The chamber is eerily quiet now, but your footsteps echo loudly against the stone. You move along the walls, your fingers tracing the ancient carvings as you look for any sign of a hidden passage. The murals on the walls seem to shift in the flickering light, their eyes following your every move. Sweat beads on your forehead as you push aside the feeling that you’re being watched.",
                                                            "You reach the far corner of the room and notice something strange—a loose stone in the floor. You press on it, and it shifts slightly, revealing a small gap beneath the surface. Your heart races as you kneel down and start pulling away the stone.",
                                                            "As soon as the stone moves, a low rumble fills the room. The ground beneath you begins to tremble, and the walls seem to close in, grinding against each other with a deafening roar. Panic surges through you as the gap you uncovered widens into a deep pit.",
                                                            "You try to scramble away, but the floor beneath your feet gives way. The chamber shakes violently as the trap activates, and the walls begin to collapse inward, sealing off any hope of escape. The last thing you hear is the sound of rushing stone and the slow, inevitable fall into the darkness below."])
                                                            wait_for_input()
                                                            game_on = handle_death()
                                        
                                        elif stone_altar == "Turn":
                                            display_text(["You decide that the risk isn’t worth it. As you step away from the altar, the vines seem to pulse with a more frantic rhythm, almost as if sensing your retreat. The low growl in the distance grows louder, more threatening, echoing off the walls and vibrating through the floor beneath your feet.",
                                            "You quicken your pace, trying to make your way back to the fork in the path. But the tunnel behind you grows darker, and the ground feels different—less solid, more like something is shifting beneath the surface.",
                                            "Suddenly, the walls begin to close in, but not in the way you expected. The very stone seems to warp and twist, turning the passage into a living maze. The vines that had been harmless before now spring to life, slithering toward you with alarming speed. Before you can react, they wrap around your ankles, tightening with a strength you hadn’t anticipated.",
                                            "You try to run, but the vines pull you back, tightening around your legs, then your torso, constricting like a serpent. Panic surges as you struggle, but the more you fight, the tighter they coil. The growl turns into a guttural roar, and from the darkness, something large and unseen moves toward you.",
                                            "In one final, crushing moment, the vines drag you toward the altar. The last thing you hear is the rhythmic pulsing turning into a deafening thrum before the vines pull you under the ground, the stone swallowing you whole."])
                                            wait_for_input()
                                            game_on = handle_death()

                                elif cave_passage == "Right":
                                    display_text(["You take the right passage, following the cool breeze. The air smells musty, but it feels fresher than the other path. The tunnel narrows as you descend, and you have to duck to avoid hitting your head on the low ceiling.",
                                    "After a while, the passage opens into a hidden underground lake. The water here is still, almost unnaturally so, and a faint light emanates from the surface. Across the lake, you see what looks like an ancient stone door embedded into the cave wall. The door is covered in intricate carvings, and you sense that something important lies beyond it."])
                                    wait_for_input()
                                        
                                    cave_pool = None
                                    display_text(["Do you choose to:", 
                                        "1. Swim across the lake to reach the stone door.",
                                        "2. Search the edge of the lake for another way around."])
                                        
                                    while cave_pool not in ['Swim', 'Search']:
                                        get_user_choice1(['Swim', 'Search'])
                                        if cave_pool == "Swim":
                                            display_text(["You decide to swim across the lake, determined to reach the stone door. The water is cool and refreshing as you dive in, but it quickly becomes apparent that there’s something off about it. The faint light emanates from the water’s surface, but as you swim deeper, the glow becomes more intense, almost blinding.",
                                            "Suddenly, you feel something brush against your leg—something cold and slippery. Panic rises in your chest as you kick harder, swimming faster. But the water begins to pull you down, the current increasing rapidly. No matter how hard you try to swim against it, you feel yourself being dragged under.",
                                            "But you refuse to give up. Summoning every ounce of strength, you push forward. The light ahead grows brighter, guiding you toward the stone door. With one final, powerful stroke, you surge through the water and reach the door. You pull yourself out of the lake, breathless but victorious.",
                                            "The door creaks open with a low rumble, revealing a dark, ancient passageway beyond. You’ve made it.",
                                            "You step through the stone door, your heart still racing from the perilous swim. The passageway beyond is narrow and winding, the walls covered in ancient carvings and symbols. The air is thick with dust and age, but the faint glow of the water's light seems to have followed you, casting an eerie illumination on the path ahead.",
                                            "As you move deeper into the passage, the sound of rushing water fades behind you, replaced by an unsettling silence. The temperature drops, and you begin to notice that the stone walls are slick with moisture, as if the cave itself is alive and breathing. You can feel the weight of the temple pressing in around you, its dark secrets just beyond reach.",
                                            "Suddenly, the corridor widens into a grand chamber. At its center stands a pedestal, upon which rests a large, intricately designed artifact—something that looks like a crown, but unlike any crown you've seen before. It's made of some dark, shimmering metal, and its edges are adorned with glowing gemstones that pulse in rhythm with your heartbeat."])
                                            wait_for_input()
                                            
                                            glowing_gemstone = None
                                            display_text(["Do you choose to:", 
                                                "1. Approach the pedestal and claim the artifact.",
                                                "2. Examine the room for traps."])

                                            while glowing_gemstone not in ['Artifact', 'Traps']:
                                                glowing_gemstone = get_user_choice1(['Artifacts', 'Traps'])
                                                if glowing_gemstone == "Artifact":
                                                    display_text(["You feel an overwhelming pull toward the artifact, a deep compulsion that seems to echo within your very soul. The crown’s gleaming gemstones call to you, their rhythm matching the beat of your heart as if they were made for you alone.",
                                                    "You step forward, cautiously at first, the weight of every choice you’ve made up to this point heavy on your shoulders. But the allure of the crown is too great. You move closer, reaching out to claim it.",
                                                    "As your fingers graze the cold surface of the crown, the room suddenly shifts. The floor trembles beneath you, and a deep rumbling sound fills the air. The gemstones on the crown glow brighter, and the temperature plummets. The once silent chamber now hums with an ominous energy.",
                                                    "Before you can react, the pedestal beneath the crown begins to sink into the ground, and the walls start to close in. The passageway behind you is sealed shut with an ancient, stone door that slams down with a deafening noise.",
                                                    "You try to move, but the crown begins to radiate an oppressive force, locking you in place. The walls around you shift, their stone faces contorting into grotesque figures as they start to creep toward you, each step accompanied by the deepening hum of the temple.",
                                                    "It’s as if the temple itself is alive, and your actions have triggered something ancient and malevolent. The glowing gemstones on the crown pulse faster and faster, like a heartbeat that has quickened with the rise of your doom.",
                                                    "A deep, guttural voice echoes from the walls, vibrating the very air. 'Fool. You have awakened that which should remain forgotten.'",
                                                    "The walls close in faster now, and the weight of the temple presses down on you. Desperately, you try to break free, but the power of the crown holds you in place. The hum grows deafening, and the temple’s fury surges like an unstoppable force.",
                                                    "With one final, crushing surge, the walls engulf you. The darkness closes in, and the last thing you hear is the low hum of the temple… and the soft, haunting rhythm of your own heartbeat, now lost in the depths of the earth."])
                                                    wait_for_input()
                                                    game_on = handle_death()

                                                elif glowing_gemstone == "Traps":
                                                    display_text(["You decide to proceed with caution. The weight of the decision presses on you, and despite the urgency of claiming the artifact, you cannot shake the feeling that something is wrong. You carefully examine the floor, the walls, and the ceiling, searching for any signs of traps.",
                                                    "The light from the crown above flickers eerily, casting long shadows across the room. Every step you take feels more deliberate, more calculated. As you scan the area, your eyes fall on a faint, almost invisible line etched into the stone floor near the pedestal. It’s barely noticeable, but it seems to form a hidden tripwire.",
                                                    "You kneel down, inspecting it more closely. You can tell that disturbing the wire would trigger something—perhaps spikes from the walls, or a falling ceiling. You carefully bypass the line, stepping over it without disturbing the mechanism. As you proceed, you find another faint marking along the walls—a small panel that can be pressed without triggering any alarm.",
                                                    "With a steady hand, you press the panel. A low rumble fills the air, and you brace yourself for whatever may come. But instead of a deadly trap, the stone wall before you slides open, revealing a hidden compartment. Inside, gleaming in the dim light, you find an ancient chest, its wood covered in moss and age, but the lock seems intact.",
                                                    "Your heart races as you approach the chest, the sense of danger lifting. You carefully open it, revealing its contents. Inside lies a collection of gold coins, priceless jewels, and, nestled at the bottom, a small but exquisitely crafted dagger with an intricate hilt. The dagger's blade gleams, untouched by time, and you feel an odd sense of power emanating from it.",
                                                    "This is the treasure you were seeking—a long-lost relic from the ancient city of Eldor. The chest is filled with artifacts unlike anything you've ever seen: intricately carved statues, rare gemstones, and golden trinkets that shimmer with an ethereal glow. But at the center of it all lies the object of your quest—the Jewel of Endor, a radiant gemstone said to hold immense power. Its light pulses gently, as if it has a heartbeat of its own.",
                                                    "You carefully lift the jewel, feeling a surge of energy flow through your fingers. The moment you touch it, the temple seems to react—the air grows warmer, and the hum of the chamber intensifies. It’s as if the very walls of the temple are alive, sensing the power now in your possession.",
                                                    "For a moment, you're paralyzed, caught between awe and fear. The treasure of Eldor is more than you ever imagined. But with it comes a warning, an unspoken truth: this artifact is no mere trinket—it holds the key to untold mysteries and dangers, and now that you have it, you are bound to the ancient forces it controls.",
                                                    "The ground beneath your feet trembles, and a voice echoes from the depths of the temple, ancient and powerful. 'The path you walk is no longer yours alone,' it whispers. 'The treasure of Endor chooses its bearer. What will you do with the power it grants?'",
                                                    "With the Jewel of Eldor in your possession, you stand at a crossroads. Will you use its power for your own gain, or will you protect it from those who seek to exploit its magic? The choice is yours, but know this: The treasure of Endor is not easily forgotten, and those who seek it will come for you."])
                                                    wait_for_input()
                                                    game_on = handle_win()

                                        elif cave_pool == "Search":
                                            display_text(["You decide to search the edge of the lake for another way around. As you step along the shore, the stillness of the water unnerves you. You trace your fingers along the cave walls, hoping to find a hidden path, but all you find are slick, wet rocks.",
                                            "The light from the water seems to grow more intense, and you feel an unnatural pressure building in the air. Suddenly, you hear a soft whisper, and before you can react, the ground beneath your feet crumbles away. The rocks give way, and you fall into a hidden pit, your body crashing into the jagged stone below.",
                                            "Pain shoots through your body as you lose consciousness, and the last thing you hear is the sound of water rising around you, sealing your fate."])
                                            wait_for_input()
                                            game_on = handle_death()
                                    
                elif attack == "Log":
                    display_text(["Desperate, you grab a burning log from the fire and hurl it at the creature, hoping the flames will deter it. The log flies through the air, but instead of hitting its mark, it lands in front of the creature, missing completely.",
                    "Enraged, the creature lets out a deafening roar and charges toward you with terrifying speed. You try to scramble back, but it's too late. The creature swipes its claws across your chest, knocking you to the ground.",
                    "You scream in agony, but it's quickly silenced as the creature finishes the attack, its jaws closing around you."])
                    wait_for_input()
                    game_on = handle_death()
    pygame.quit()
    sys.exit()          


    
start_of_game()
game()
pygame.quit()

    
    

    
    
    
    
