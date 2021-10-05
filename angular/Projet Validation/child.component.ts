import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }
  GenderData: any[] = ['Male’, ‘Female'];

  check = {
    FirstName: '', LastName: '', address: '', city: '', state: '', postcode: null, Gender: null, // ligne ajoute


    constructor() { }
  ngOnInit(): void { }

  }

  export interface addresscheck {
  FirstName: string,
  LastName: string,
  address: string,
  city: string,
  state: string,
  postcode: number,
  Gender: any[],
}
