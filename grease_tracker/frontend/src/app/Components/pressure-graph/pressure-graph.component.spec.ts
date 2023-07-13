import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PressureGraphComponent } from './pressure-graph.component';

describe('PressureGraphComponent', () => {
  let component: PressureGraphComponent;
  let fixture: ComponentFixture<PressureGraphComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PressureGraphComponent],
    });
    fixture = TestBed.createComponent(PressureGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
