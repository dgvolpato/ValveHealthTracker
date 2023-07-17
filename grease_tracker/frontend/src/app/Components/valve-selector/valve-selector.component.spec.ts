import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ValveSelectorComponent } from './valve-selector.component';

describe('ValveSelectorComponent', () => {
  let component: ValveSelectorComponent;
  let fixture: ComponentFixture<ValveSelectorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ValveSelectorComponent]
    });
    fixture = TestBed.createComponent(ValveSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
