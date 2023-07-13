import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GreaseGraphComponent } from './grease-graph.component';

describe('GreaseGraphComponent', () => {
  let component: GreaseGraphComponent;
  let fixture: ComponentFixture<GreaseGraphComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GreaseGraphComponent]
    });
    fixture = TestBed.createComponent(GreaseGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
