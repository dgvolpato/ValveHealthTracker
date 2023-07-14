import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GreaseCapacityGuageComponent } from './grease-capacity-guage.component';

describe('GreaseCapacityGuageComponent', () => {
  let component: GreaseCapacityGuageComponent;
  let fixture: ComponentFixture<GreaseCapacityGuageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GreaseCapacityGuageComponent]
    });
    fixture = TestBed.createComponent(GreaseCapacityGuageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
