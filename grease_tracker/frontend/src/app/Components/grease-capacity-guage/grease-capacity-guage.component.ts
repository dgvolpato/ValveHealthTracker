import { Component, Input, SimpleChanges } from '@angular/core';
import * as Highcharts from 'highcharts';
import HC_more from 'highcharts/highcharts-more';
import ChartModuleMore from 'highcharts/highcharts-more.js';
import HCSoldGauge from 'highcharts/modules/solid-gauge';
ChartModuleMore(Highcharts);
HCSoldGauge(Highcharts);
HC_more(Highcharts);

@Component({
  selector: 'app-grease-capacity-guage',
  templateUrl: './grease-capacity-guage.component.html',
  styleUrls: ['./grease-capacity-guage.component.scss'],
})
export class GreaseCapacityGuageComponent {
  @Input() selectedValve: string = '';

  selectedOption: number = -1;
  pressureGraph: typeof Highcharts = Highcharts;

  chartOptions: Highcharts.Options = {};

  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges): void {
    this.selectedOption = this.selectedValve.charCodeAt(0) - 65;
    this.loadGraph();
  }

  loadGraph(): void {
    const greaseAvailable = Object.values(greaseCapacity)[this.selectedOption];
    this.chartOptions = {
      title: {
        text: 'Greasing Capacity',
      },
      chart: {
        width: 300,
        height: 300,
      },
      pane: {
        center: ['50%', '85%'],
        size: '100%',
        startAngle: -90,
        endAngle: 90,
        background: [
          {
            backgroundColor: '#EEE',
            innerRadius: '60%',
            outerRadius: '100%',
            shape: 'arc',
          },
        ],
      },

      exporting: {
        enabled: false,
      },

      tooltip: {
        enabled: false,
      },

      // the value axis
      yAxis: {
        stops: [
          [0.1, '#DF5353'], // red
          [0.5, '#DDDF0D'], // yellow
          [0.9, '#55BF3B'], // green
        ],
        lineWidth: 0,
        tickWidth: 0,
        minorTickInterval: null,
        tickAmount: 2,
        title: {
          y: -10,
        },
        labels: {
          y: 16,
        },
        min: 0,
        max: 100,
      },

      plotOptions: {
        solidgauge: {
          dataLabels: {
            y: 0,
            borderWidth: 0,
            useHTML: true,
          },
        },
      },
      series: [
        {
          type: 'solidgauge',
          data: [greaseAvailable],
          dataLabels: {
            format:
              '<div style="text-align:center">' +
              '<span style="font-size:25px">{y}%</span><br/>' +
              '<span style="font-size:12px;opacity:0.4">Grease left</span>' +
              '</div>',
          },
          tooltip: {
            valueSuffix: 'g',
          },
        },
      ],
    };
  }
}

export const greaseCapacity = {
  A: 90,
  B: 50,
  C: 10,
};
