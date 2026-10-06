#include <iostream>
#include <bits/stdc++.h>
#include <array>
#include <vector>
#include <cmath>

using namespace std;

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
    
    
    void display_stats() {
        cout << "\n"  << name << " (" << element << ") - HP: " << hp << "/" << fullHP << ", Attack: " << attack << ", Defense: " << defense << ", Speed: " << speed << endl;
        cout << "Moves: ";

        for (auto& [move, power]: moveSet) {
            cout << move << "(" << power << "), ";
        }
        
        cout << endl;
    }
    
    
    void attacks(Bender& defender, int move_index) {
        string move = moveSet[move_index].first;
        int move_power = moveSet[move_index].second;
    
        cout << "\n" << name << " used " << move << "!\n";
        int damage = round((double)(attack * move_power) / defender.defense);
        defender.hp = max(0, defender.hp - damage);
        cout << "\n" << defender.name << " took " << damage << " damage\n";
    }
    
    
    void is_fainted() {
        if (hp <= 0) {
            cout << "\n" << name << " fainted: True";
        } else {
            cout << "\n" << name << " fainted: False";
        }
    }
};



int main() {
    // Create Kael
    Bender kael("Kael", "Fire", 100, 58, 38, 88, {{"Ember Slash", 40}, {"Quick Jab", 30}, {"Focus", 0}, {"Flame Surge", 70}});
    
    // Create Mira
    Bender mira("Mira", "Water", 92, 50, 45, 60, {{"Water Whip", 35}, {"Tide Push", 25}, {"Mist Veil", 0}, {"Tidal Wave", 60}});
    
    // Display initial stats
    kael.display_stats();
    mira.display_stats();
    
    // Kael attacks Mira with Ember Slash
    kael.attacks(mira, 0);
    mira.display_stats();

    // Check if Mira fainted
    mira.is_fainted();

    return 0;
}
