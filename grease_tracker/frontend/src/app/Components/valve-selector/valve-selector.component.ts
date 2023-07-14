import { Component, EventEmitter, Output } from '@angular/core';
import * as TestData from '../../Data/test-data';

@Component({
  selector: 'app-valve-selector',
  templateUrl: './valve-selector.component.html',
  styleUrls: ['./valve-selector.component.scss'],
})
export class ValveSelectorComponent {
  valvesAvailableForSelection: string[] = [];
  selectedValve: string = '';
  @Output() selectedValveEvent: EventEmitter<string> = new EventEmitter();

  ngOnInit(): void {
    const valves = Object.keys(TestData.psiData);
    this.valvesAvailableForSelection = valves.map((name) => 'Valve ' + name);
  }

  selectValve(event: Event): void {
    const target = event.target as HTMLElement;
    this.selectedValve = target.innerText.split(' ')[1];
    this.selectedValveEvent.emit(this.selectedValve);
  }
}
