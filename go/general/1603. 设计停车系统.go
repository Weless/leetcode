package main

type ParkingSystem struct {
	big    int
	medium int
	samll  int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{big, medium, small}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	switch carType {
	case 1:
		if this.big == 0 {
			return false
		} else {
			this.big -= 1
			return true
		}
	case 2:
		if this.medium == 0 {
			return false
		} else {
			this.medium -= 1
			return true
		}
	case 3:
		if this.samll == 0 {
			return false
		} else {
			this.samll -= 1
			return true
		}
	}
	return false
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */
