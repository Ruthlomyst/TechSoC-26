#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <cmath>

using namespace std;

// Generates a random integer between lo and hi, used for random moves,
// critical hits, and deciding who goes first when speeds are equal.
int random_int(int lo, int hi) {
    static mt19937 rng(random_device{}());
    return uniform_int_distribution<int>(lo, hi)(rng);
}

// Gives the attack a 10% chance of being a critical hit.
// A critical hit doubles the final damage and increases the counter.
double criticalHit(int& cHits) {
    if (random_int(1,10) == 3) {
        cout << "Critical Hit!" << endl;
        cHits++;
        return 2.0;
    } 
    
    return 1.0;
}


// Bender stores the stats and moves of each character.
class Bender {
    
public:
    string name;
    string element;
    int hp;
    int attack; 
    int defense;
    int speed;
    int fullHP;
    vector<pair<string, int>> moveSet;

    Bender(string name, string element, int hp, int attack, int defense, int speed, vector<pair<string, int>> moveSet) {
        this->name = name;
        this->element = element;
        this->hp = hp;
        this->attack = attack;
        this->defense = defense;
        this->speed = speed;
        this->moveSet = moveSet;
        fullHP = hp;
    }

    // A Bender is considered defeated when their HP reaches 0 or below.
    bool is_fainted() {return hp <= 0;}
};


// Duel controls the complete battle between two Benders.
class Duel {
    
public:
    Bender& player1;
    Bender& player2;
    int cHits = 0;
    int seHits = 0;

    Duel(Bender& play1, Bender& play2) : player1(play1), player2(play2) {}

    void duelSettings(Bender& attacker, Bender& defender, int turn) {
        
        if (turn == 1) cout << "";
        else
            cout << "Turn " << turn << ": " << attacker.name << " attacks!\n";
        
        // One of the four moves is randomly selected for every turn.
        int move_index = random_int(0, 3);
        cout << "\n" << attacker.name << " used " << attacker.moveSet[move_index].first << "!\n";

        // The element matchup determines whether the attack is stronger or weaker.
        double enhancer = effectiveness(attacker.element, defender.element, seHits);
        
        // Damage is based on attack power, move power, and defender's defense.
        int base_damage = (attacker.attack * attacker.moveSet[move_index].second) / defender.defense;

        // The base damage is then modified by elemental effectiveness
        // and the critical-hit multiplier.
        int final_damage = round(base_damage * enhancer * criticalHit(cHits));
        
        defender.hp = max(0, defender.hp - final_damage);
        cout << defender.name << " took " << final_damage << " damage" << endl;
        cout << defender.name << " HP: " << defender.hp << "/" << defender.fullHP << "\n" << endl; 
        
        // After every attack, check if the defender has been defeated.
        if (defender.is_fainted()) {
            cout << defender.name << " fainted!\n";
            cout << "🏆 " << attacker.name << " wins the duel!\n";
            
            cout << "Duel Summary: \n" << " - Winner: " << attacker.name << endl;
            cout << " - Turns: " << turn << endl;
            cout << " - Critical Hits: " << cHits << endl;
            cout << " - Super Effective Hits: " << seHits << endl;
        } else {
            // If the defender survives, the roles are swapped and the next turn begins.
            duelSettings(defender, attacker, turn+1);
        }
    }
    
    
    void start_duel() {
        cout << "\n=== DUEL BEGINS! ===" << endl;
        cout << "\n" << player1.name << " (" << player1.element << ", HP: " << player1.hp << "/" << player1.fullHP << ") VS ";
        cout << player2.name << " (" << player2.element << ", HP: " << player2.hp << "/" << player2.fullHP << ")\n";
        
        // Speed determines who gets the first attack.
        // If both Benders have the same speed, the first attacker is random.
        if (player1.speed > player2.speed) {
            cout << "Turn 1: " << player1.name << " goes first! (Speed: " << player1.speed << " v " << player2.speed << ")\n";
            duelSettings(player1, player2, 1);
        } else if (player2.speed > player1.speed) {
            cout << "Turn 1: " << player2.name << " goes first! (Speed: " << player2.speed << " v " << player1.speed << ")\n";
            duelSettings(player2, player1, 1);
        } else {
            int x = random_int(1, 2);
            
            if (x == 1) {
                cout << "Turn 1: Speed tie! " << player1.name << " goes first! (Speed: " << player1.speed << " vs " << player2.speed << ")\n";
                duelSettings(player1, player2, 1);
            } else if (x == 2) {
                cout << "Turn 1: Speed tie! " << player2.name << " goes first! (Speed: " << player1.speed << " vs " << player2.speed << ")\n";
                duelSettings(player2, player1, 1);
            }
        }
    }
    
    
    // Checks the relationship between the attacker's and defender's elements.
    // A strong matchup gives 2x damage, a weak matchup gives 0.5x damage,
    // and a neutral matchup leaves the damage unchanged.
    double effectiveness(string element1, string element2, int& seHits) {
        
        if (element1 == "Fire" and element2 == "Water") {
            cout << "Not very effective... (Fire is weak against Water)\n";
            return 0.5;
        } else if (element1 == "Water" and element2 == "Fire") {
            cout << "Super Effective! (Water is strong against Fire)\n";
            seHits++;
            return 2;
        }
        
        if (element1 == "Air" and element2 == "Fire") {
            cout << "Not very effective... (Air is weak against Fire)\n";
            return 0.5;
        } else if (element1 == "Fire" and element2 == "Air") {
            cout << "Super Effective! (Fire is strong against Air)\n";
            seHits++;
            return 2;
        }
        
        if (element1 == "Earth" and element2 == "Air") {
            cout << "Not very effective... (Earth is weak against Air)\n";
            return 0.5;
        } else if (element1 == "Air" and element2 == "Earth") {
            cout << "Super Effective! (Air is strong against Earth)\n";
            seHits++;
            return 2;
        }
        
        if (element1 == "Water" and element2 == "Earth") {
            cout << "Not very effective... (Water is weak against Earth)\n";
            return 0.5;
        } else if (element1 == "Earth" and element2 == "Water") {
            cout << "Super Effective! (Earth is strong against Water)\n";
            seHits++;
            return 2;
        }
        
        // If there is no special elemental relationship, damage stays normal.
        return 1;
    }
    
};


int main() {
    
    // Create the first pair of Benders.
    // Nadia and Talon have equal speed, so their first attacker is random.
    Bender nadia("Nadia", "Water", 85, 48, 60, 72,
                 {{"Wave Crash", 35}, {"Splash Kick", 25}, {"Guard", 0}, {"Riptide", 50}});

    Bender talon("Talon", "Air", 90, 52, 55, 72,
                 {{"Gale Strike", 38}, {"Wind Cutter", 28}, {"Updraft", 0}, {"Cyclone Blast", 48}});

    Duel duel(nadia, talon);
    duel.start_duel();
    
    
    // Create the second pair of Benders.
    // Kael is Fire and Mira is Water, so Water has an elemental advantage.
    Bender kael("Kael", "Fire", 100, 58, 38, 88,
                {{"Ember Slash", 40}, {"Quick Jab", 30}, {"Focus", 0}, {"Flame Surge", 70}});

    Bender mira("Mira", "Water", 92, 50, 45, 60,
                {{"Water Whip", 35}, {"Tide Push", 25}, {"Mist Veil", 0}, {"Tidal Wave", 60}});

    // Start the second duel. Kael has higher speed, so Kael attacks first.
    Duel duel2(kael, mira);
    duel2.start_duel();

    return 0;
}
