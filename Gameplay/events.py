import random

def generate_event():
    """
    Randomly selects an event that can happen during the game.
    
    Events represent encounters or situations the player may face, which 
    can have positive or negative outcomes. Examples include finding items,
    meeting characters, or encountering dangers.

    Returns:
        str: The name of the randomly selected event.
    """
    events = [
        "Find Healing Potion",
        "Discover a Weapon",
        "Encounter a Trap",
        "Meet a Merchant",
        "Mysterious Chest",
        "Ambushed by Bandits",
        "Blessing from a Sage",
        "Cursed Relic",
        "Treasure Found",
        "Wandering Spirit",
        "Nimble Training",
        "Sharpen Focus"
    ]
    return random.choice(events)

def apply_item_effect(player, item):
    """
    Applies the effects of an item to the player's stats.

    The item's effects are applied to the corresponding stats, updating 
    them accordingly. Positive effects increase stats, while negative 
    effects decrease them.

    Args:
        player (Character): The player instance receiving the item's effect.
        item (dict): The item with its name and effect attributes.
    """
    effect = item.get("effect", {})
    print(f"\nYou received {item['name']}!")
    for key, value in effect.items():
        player.stats[key] = max(0, player.stats.get(key, 0) + value)
        print(f"{key} {'increased' if value > 0 else 'decreased'} by {abs(value)}.")
    print(f"Updated stats: {player.stats}")

def handle_event(player):
    """
    Triggers a random event and processes its effects on the player.
    
    Depending on the event, the player may receive an item, encounter a
    hazard, or interact with a character. Player choices may influence 
    the outcome of some events.

    Args:
        player (Character): The player instance experiencing the event.
    """
    event = generate_event()
    print(f"\nEvent: {event}")

    if event == "Find Healing Potion":
        item = {"name": "Healing Potion", "effect": {"HP": 20}}
        apply_item_effect(player, item)

    elif event == "Discover a Weapon":
        item = {"name": "Legendary Sword", "effect": {"ATK": 15}}
        apply_item_effect(player, item)

    elif event == "Encounter a Trap":
        item = {"name": "Trap Damage", "effect": {"HP": -15}}
        apply_item_effect(player, item)

    elif event == "Meet a Merchant":
        print("You met a merchant! He offers to sell you an item:")
        merchant_items = [
            {"name": "Merchant's Weapon", "effect": {"ATK": 10}},
            {"name": "Focus Elixir", "effect": {"CRIT": 10}},
            {"name": "Evasion Boots", "effect": {"DODGE": 10}}
        ]
        for i, item in enumerate(merchant_items, 1):
            print(f"{i}. {item['name']} ({item['effect']})")
        choice = input("Choose an item to buy (1/2/3) or type 'no' to skip: ").strip().lower()
        if choice in ["1", "2", "3"]:
            item = merchant_items[int(choice) - 1]
            apply_item_effect(player, item)
        else:
            print("You walk away from the merchant.")

    elif event == "Mysterious Chest":
        print("You found a mysterious chest!")
        choice = input("Do you open it? (yes/no): ").strip().lower()
        if choice == "yes":
            # Random reward or punishment
            chest_rewards = [
                {"name": "Treasure", "effect": {"HP": 30, "ATK": 10}},
                {"name": "Focus Elixir", "effect": {"CRIT": 10}},  # Boost crit chance
                {"name": "Evasion Boots", "effect": {"DODGE": 10}},  # Boost dodge ability
                {"name": "Poison Gas", "effect": {"HP": -20}}
            ]
            item = random.choice(chest_rewards)
            apply_item_effect(player, item)
        else:
            print("You leave the chest untouched.")

    elif event == "Ambushed by Bandits":
        print("You were ambushed by bandits! You lose some HP.")
        item = {"name": "Bandit Attack", "effect": {"HP": -25}}
        apply_item_effect(player, item)

    elif event == "Blessing from a Sage":
        print("A sage blesses you with magical energy!")
        item = {"name": "Sage's Blessing", "effect": {"HP": 20, "ATK": 10}}
        apply_item_effect(player, item)

    elif event == "Cursed Relic":
        print("You found a cursed relic! It drains your energy.")
        item = {"name": "Cursed Relic", "effect": {"HP": -15, "ATK": -5}}
        apply_item_effect(player, item)

    elif event == "Treasure Found":
        print("You found a hidden treasure!")
        item = {"name": "Gold Coins", "effect": {"HP": 10}}
        apply_item_effect(player, item)

    elif event == "Wandering Spirit":
        print("A wandering spirit offers you power at a cost.")
        choice = input("Do you accept its gift? (yes/no): ").strip().lower()
        if choice == "yes":
            item = {"name": "Spirit's Power", "effect": {"ATK": 20, "HP": -10}}
            apply_item_effect(player, item)
        else:
            print("The spirit vanishes into the void.")

    elif event == "Nimble Training":
        print("You attended a training session to improve your agility!")
        item = {"name": "Agility Boost", "effect": {"DODGE": 15}}
        apply_item_effect(player, item)

    elif event == "Sharpen Focus":
        print("You spent time sharpening your focus, enhancing your critical strikes!")
        item = {"name": "Focus Training", "effect": {"CRIT": 15}}
        apply_item_effect(player, item)
