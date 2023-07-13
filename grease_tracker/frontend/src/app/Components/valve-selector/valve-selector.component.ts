import { Component, EventEmitter, Output } from '@angular/core';
import * as TestData from '../../Data/test-data';

@Component({
  selector: 'app-valve-selector',
  templateUrl: './valve-selector.component.html',
  styleUrls: ['./valve-selector.component.scss'],
})
export class ValveSelectorComponent {
  valvesAvailableForSelection: string[] = [];
  @Output() selectedValveEvent: EventEmitter<string> = new EventEmitter();

  ngOnInit(): void {
    this.valvesAvailableForSelection = Object.keys(TestData.psiData);
  }

  selectValve(event: Event): void {
    const target = event.target as HTMLElement;
    this.selectedValveEvent.emit(target.innerText);
  }
}
