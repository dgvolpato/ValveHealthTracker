import { Component } from '@angular/core';
import * as TestData from '../../Data/test-data';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss'],
})
export class HomePageComponent {
  selectedPressureData = TestData.psiData.A;
  selectedGreaseData = TestData.psiData.A;
  selectedGreasingValve: string = '';
  selectedValve: string = '';

  setSelectedValve(event: string): void {
    this.selectedValve = event;
  }
}
