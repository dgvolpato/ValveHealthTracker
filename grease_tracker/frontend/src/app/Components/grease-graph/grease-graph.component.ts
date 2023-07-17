import { Component, Input, SimpleChanges } from '@angular/core';
import * as Highcharts from 'highcharts';
import * as TestData from '../../Data/test-data';

@Component({
  selector: 'app-grease-graph',
  templateUrl: './grease-graph.component.html',
  styleUrls: ['./grease-graph.component.scss'],
})
export class GreaseGraphComponent {
  @Input() greaseData: string = '';

  selectedOption: number = -1;
  greaseGraph: typeof Highcharts = Highcharts;
  updateFlag = false;

  chartOptions: Highcharts.Options = {};

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges): void {
    console.log(this.greaseData);
    this.selectedOption = this.greaseData.charCodeAt(0) - 65;
    this.loadGraph();
  }

  loadGraph(): void {
    const greaseData = Object.values(TestData.greaseData)[this.selectedOption];
    const greasingPressureData = greaseData?.map(
      (res: { timestamp: any; value: number }) => [
        res.timestamp,
        res.value > 0 ? res.value : 0,
      ]
    );

    this.chartOptions = {
      title: {
        text: 'Greasing at Cavity Graph',
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
