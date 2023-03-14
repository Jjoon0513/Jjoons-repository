using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    void Update()
    {
        transform.Rotate(new Vector3(10f, 20f, 30f) * Time.deltaTime);

        transform.Rotate(new Vector3(10f, 20f, 30f) * Time.deltaTime, Space.World);
    }
}
