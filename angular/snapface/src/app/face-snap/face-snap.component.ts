import { Component, OnInit,Input } from '@angular/core';
import { FaceSnap } from '../models/snap-face-model';


@Component({
  selector: 'app-face-snap',
  templateUrl: './face-snap.component.html',
  styleUrls: ['./face-snap.component.scss']
})
export class FaceSnapComponent implements OnInit{
 @Input() faceSnap!: FaceSnap;
  
  // Ajoutez les propriete 
    title!: string;
    description!: string;
    createdDate!: Date;
    snaps!:number;
    imageUrl!: string;
    buttonText!: string;
    
    //Puis creer  l'attribut avec les differents propriete 
      ngOnInit(): void {
      this.title = 'Bahar ';
      this.description ='notre boube';
      this.createdDate = new Date();
      this.snaps = 6;
      this.imageUrl = 'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg';
      this.buttonText = "Oh snap!";
      }
      onsnap()   {
        if (this.buttonText === "Oh snap!" ){
        this.faceSnap.snaps ++;
        this.buttonText = "Oops, unsnap!";
        }
        
        else {
          this.faceSnap.snaps --;
          this.buttonText = "Oh snap!";
        }
      }
  
  }


    
    
    
    
  

