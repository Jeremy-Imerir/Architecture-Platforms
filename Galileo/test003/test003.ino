// Charger la librairie LiquidCrystal
#include <LiquidCrystal.h>

// D√©finir les pins utilis√©es par le LCD
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

// D√©finir les variables globales pour l'affichage du LCD
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
boolean client_present = true;

int xMin_Map = 0;
int xMax_Map = 100;

int read_LCD_buttons()// Fonction lire les boutons
{
  adc_key_in = analogRead(0); // Lire les valeurs du capteurs
  // Les valeurs renvoy√©es sont sens√©s etre: 0, 144, 329, 504, 741
  // Il y a une erreur possible de 50
  if (adc_key_in > 1000) return btnNONE; // Nous d√©coupons les valeurs possibles en zone pour chaque bouton
  if (adc_key_in < 50) return btnRIGHT;
  if (adc_key_in < 250) return btnUP;
  if (adc_key_in < 450) return btnDOWN;
  if (adc_key_in < 650) return btnLEFT;
  if (adc_key_in < 850) return btnSELECT;
  return btnNONE; // On renvoie cela si l'on est au dessus de 850
}

void libroccuper(boolean etat)
{
  lcd.setCursor(0,0); // Placer le curseur au d√©but de la premi√®re ligne
  if (etat == true)
  {
    lcd.print("Etat : Libre  ");
  }
  else
  {
    lcd.print("Etat : Occuper"); 
  }
}

int calculeDistanceX (int xT, int mT, int xC, int mC)
{
  int xDiff = 0;
  int mDiff = 0;
  
  mDiff = mT - mC;
  
  switch (mDiff)
  {
    case -2: // | T |...| C |
    {
      xDiff = xMax_Map - xT + xMax_Map + xC;
      break;
    }
    case -1: // | T | C |...| ou  |...| T | C |
    {
      xDiff = xMax_Map - xT + xC;
      break;
    }
    case 0:  // | TC |...|...| ou |...| TC |...| ou |...|...| TC |
    {
      if (xT>xC)
      xDiff = xT - xC;
      else
      xDiff = xC - xT;
      break;
    }
    case 1: // | C | T |...| ou |...| C | T |
    {
      xDiff = xT + xMax_Map - xC;
      break;
    }
    case 2: // | C |...| T |
    {
      xDiff = xT + xMax_Map + xMax_Map - xC;
      break;
    }
  }
  return xDiff;
}

void setup() // Initialisation
{
  lcd.begin(16, 2); // D√©marrer la librairie
  lcd.setCursor(0,0); // Placer le curseur au d√©but de la premi√®re ligne
  lcd.print("Initialisation"); // Afficher un message simple
}

void loop() // Fonction principale
{
  
  if (client_present)
  {
    lcd_key = read_LCD_buttons(); // Lire les boutons
    libroccuper(etat_taxi);
    
    if (etat_taxi)
    {
      lcd.setCursor(0,1); // Placer le curseur au d√©but de la seconde ligne
      lcd.print("Client? O/N ");
      switch (lcd_key) // Selon le bouton appuyer
      {
        case btnLEFT: // Pour le bouton "Left"
        {
          lcd.setCursor(0,1); // Placer le curseur au d√©but de la seconde ligne
          lcd.print("Client accept√© ");
          etat_taxi = false;
          break;
        }
        case btnRIGHT: // Pour le bouton "Right"
        {
          lcd.setCursor(0,1); // Placer le curseur au d√©but de la seconde ligne
          lcd.print("Client refoul ");    
          etat_taxi = true;
          break;
        }
      }
    }
    else
    {
       lcd.setCursor(0,1); // Placer le curseur au d√©but de la seconde ligne
       lcd.print("Client dans file d'attente "); // Afficher "Right"
    }  
  }
  else
  {
    lcd.setCursor(0,1); // Placer le curseur au d√©but de la seconde ligne
    lcd.print("Pas de clients ");
  }
}


