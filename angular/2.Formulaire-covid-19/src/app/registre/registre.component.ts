import { Component, OnInit } from '@angular/core';
import { Client } from '../model/clients';

@Component({
  selector: 'app-registre',
  templateUrl: './registre.component.html',
  styleUrls: ['./registre.component.css']
})
export class RegistreComponent  {

  model = new Client('Abdullahi','Amir',123,'Borama','Somali','Canadienne','mkoi',);

  

}
