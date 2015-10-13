// Charger la librairie LiquidCrystal
#include <LiquidCrystal.h>

// Définir les pins utilisées par le LCD
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

// Définir les variables globales pour l'affichage du LCD
int lcd_key = 0;
int adc_key_in = 0;
#define btnRIGHT 0
#define btnUP 1
#define btnDOWN 2
#define btnLEFT 3
#define btnSELECT 4
#define btnNONE 5
// Autres variables globales
boolean etat_taxi = true;
boolean client = false;

int read_LCD_buttons()// Fonction lire les boutons
{
  adc_key_in = analogRead(0); // Lire les valeurs du capteurs
  // Les valeurs renvoyées sont sensés etre: 0, 144, 329, 504, 741
  // Il y a une erreur possible de 50
  if (adc_key_in > 1000) return btnNONE; // Nous découpons les valeurs possibles en zone pour chaque bouton
  if (adc_key_in < 50) return btnRIGHT;
  if (adc_key_in < 250) return btnUP;
  if (adc_key_in < 450) return btnDOWN;
  if (adc_key_in < 650) return btnLEFT;
  if (adc_key_in < 850) return btnSELECT;
  return btnNONE; // On renvoie cela si l'on est au dessus de 850
}

void libroccuper(boolean etat)
{
  lcd.setCursor(0,0); // Placer le curseur au début de la première ligne
  if (etat == true)
  {
    lcd.print("Etat : Libre  ");
  }
  else
  {
    lcd.print("Etat : Occuper"); 
  }
}

void setup() // Initialisation
{
  lcd.begin(16, 2); // Démarrer la librairie
  lcd.setCursor(0,0); // Placer le curseur au début de la première ligne
  lcd.print("Initialisation"); // Afficher un message simple
}

void loop() // Fonction principale
{
  lcd_key = read_LCD_buttons(); // Lire les boutons
  libroccuper(etat_taxi);
  
  lcd.setCursor(0,1); // Placer le curseur au début de la seconde ligne
  
  switch (lcd_key) // Selon le bouton appuyer
  {
    case btnRIGHT: // Pour le bouton "Right"
    {
      lcd.print("RIGHT "); // Afficher "Right"
      etat_taxi = true;
      break;
    }
    case btnLEFT: // Pour le bouton "left"
    {
      lcd.print("LEFT "); // Afficher "Left"      
      etat_taxi = false;
      break;
    }
  }
  
  
  
}

