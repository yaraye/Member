import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {MembersComponent} from './members/members.component';
import {MembersListComponent} from './members-list/members-list.component'


const routes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'members', component: MembersComponent},
  {path: 'membersList', component: MembersListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
