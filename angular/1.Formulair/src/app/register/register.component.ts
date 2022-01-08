import { Component } from '@angular/core';
import {User} from '../models/user';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent  {
  
  
  
  
  
  provinces = [ 'Alberta', 'Colombie-Britannique', 'Île-du-Prince-Édouard', 'Manitoba', 'Nouveau-Brunswick','Nouvelle-Écosse', 'Ontario', 'Québec','Saskatchewan', 'Terre-Neuve-et-Labrador'];
  
  model = new User(18, 'amir', 'abdullahi', this.provinces[0], 1000);
  
   Submit = false
  
  onSubmit() {this.Submit = true}

  

}
