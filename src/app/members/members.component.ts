import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';


@Component({
  selector: 'app-members',
  templateUrl: './members.component.html',
  styleUrls: ['./members.component.css']
})
export class MembersComponent implements OnInit {
members:object;
firstName:any;
lastName
reasonArray:any;
amount:number;
// date:Date;
received_by: any;


  constructor(private router:Router) { 
  this.firstName = '',
  this.lastName='',
  this.reasonArray = ['Select one ','Donation', 'Members Fee', 'Collection'],
  this.amount = 0,
  // this.date = '',
  this.received_by =''
 
  }

  ngOnInit() {

  }
  handleSubmit(){
    this.router.navigate(['/membersList']);
  }

}
