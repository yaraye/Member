import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {AuthenticationService} from '../authentication.service';
// import{LocalStorageService} from 'angular-2-local-storage';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user: object;

  constructor(
    private router: Router, private auth: AuthenticationService) {
  // creating empty variable 
    this.user = {
      'email': '',
      'password': ''
    };
    console.log('hello')
   }

  ngOnInit() {
    
  }
  handleSubmit(){
    console.log('clicked');
    this.auth.login(this.user['email'], this.user['password']).subscribe((data)=> {   
      console.log(data);
      this.router.navigate(['/members'])
    }
    )}

}



