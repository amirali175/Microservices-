import { Component, OnInit,Input} from '@angular/core';
import { FaceSnap } from 'src/models/face-snap.models';


@Component({
  selector: 'app-face-snap',
  templateUrl: './face-snap.component.html',
  styleUrls: ['./face-snap.component.scss']
})
export class FaceSnapComponent implements OnInit {
  @Input () faceSnap!:FaceSnap;
  
  // creer les propriete de faceSnap
  title!: string;
  description!:string;
  createdDate!: Date;
  imageUrl!: string;
  snap!:number;
  buttonText!: string;

  //Dans le ngOnInit attribut les donnees 
  

  ngOnInit(): void {
    this.title = "TimHorton's";
    this.description = "compagnie Commercial ";
    this.createdDate = new Date();
    this.imageUrl =  'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg';
    this.snap = 6;
    this.buttonText = "Oh Snap!"
  }
  onSnap() {
    if (this.buttonText === 'Oh Snap!') {
      this.faceSnap.snap++;
      this.buttonText = 'Oops, unSnap!';
    } else {
      this.faceSnap.snap--;
      this.buttonText = 'Oh Snap!'
    }
  }
}