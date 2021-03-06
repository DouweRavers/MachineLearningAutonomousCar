using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CarBase))]
public class HumanCarController : MonoBehaviour {

	CarBase car;
	public float steerValue = 0;
	void Start() {
		if (UI.player != 0) Destroy(gameObject);
		car = GetComponent<CarBase>();
	}

	void Update() {
		if (Input.GetKeyDown(KeyCode.Tab)) car.toggleEngine();
		steerValue = Input.GetAxis("Horizontal");
		car.steerCar(steerValue);
	}

}
