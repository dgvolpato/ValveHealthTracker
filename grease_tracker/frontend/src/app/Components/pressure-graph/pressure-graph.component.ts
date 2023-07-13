import { Component, Input, SimpleChanges } from '@angular/core';
import * as Highcharts from 'highcharts';
import * as TestData from '../../Data/test-data';

@Component({
  selector: 'app-pressure-graph',
  templateUrl: './pressure-graph.component.html',
  styleUrls: ['./pressure-graph.component.scss'],
})
export class PressureGraphComponent {
  @Input() pressureData: string = '';

  selectedOption: number = -1;
  pressureGraph: typeof Highcharts = Highcharts;
  updateFlag = false;

  chartOptions: Highcharts.Options = {};

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges): void {
    this.selectedOption = this.pressureData.charCodeAt(0) - 65;
    this.loadGraph();
  }

  loadGraph(): void {
    const pressureData = Object.values(TestData.psiData)[this.selectedOption];
    console.log(this.selectedOption, pressureData);
    const greasingPressureData = pressureData?.map(
      (res: { timestamp: any; value: number }) => [
        res.timestamp,
        res.value > 0 ? res.value : 0,
      ]
    );

    this.chartOptions = {
      title: {
        text: 'Pressure On Valve Graph',
        align: 'left',
      },

      subtitle: {
        text: 'Pressure vs Timestamp',
        align: 'left',
      },

      xAxis: {
        title: {
          text: 'Timestamp',
        },
      },
      yAxis: {
        title: {
          text: 'Pressure (PSI)',
        },
      },
      series: [
        {
          type: 'line',
          data: greasingPressureData,
        },
      ],
    };
  }
}
