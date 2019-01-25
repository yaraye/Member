import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(private http: HttpClient) {
    
   }
   login(username, password) {
    //this returns a promise
    return this.http.post('https://reqres.in/api/login',
    {'email' : username, 'password': password});
  }
}
