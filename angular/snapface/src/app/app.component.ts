import { Component , OnInit } from '@angular/core';
import { FaceSnap } from './models/snap-face-model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  mySnap!: FaceSnap;
  myOtherSnap!:FaceSnap;

  
  ngOnInit() {
    
      this.mySnap = new FaceSnap(
        'Bahar',
        'notre boube ',
        'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg',
        new Date(),
        0

  );
  this.myOtherSnap = new FaceSnap(
    'Bahar11',
    'notre boube ',
    'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg',
    new Date(),
    0
  );
  }

  
}
