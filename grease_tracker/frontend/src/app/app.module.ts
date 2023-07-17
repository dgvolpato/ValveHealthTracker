import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HighchartsChartModule } from 'highcharts-angular';
import { MatCardModule } from '@angular/material/card';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './Components/home-page/home-page.component';
import { PressureGraphComponent } from './Components/pressure-graph/pressure-graph.component';
import { GreaseGraphComponent } from './Components/grease-graph/grease-graph.component';
import { ValveSelectorComponent } from './Components/valve-selector/valve-selector.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { GreaseCapacityGuageComponent } from './Components/grease-capacity-guage/grease-capacity-guage.component';
import { HeaderComponent } from './Components/header/header.component';

@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    PressureGraphComponent,
    GreaseGraphComponent,
    ValveSelectorComponent,
    GreaseCapacityGuageComponent,
    HeaderComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HighchartsChartModule,
    BrowserAnimationsModule,
    MatCardModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
