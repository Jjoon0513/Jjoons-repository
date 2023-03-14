using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    void Update()
    //한틱마다 업데이트됩니다.
    {
        //Time.deltaTime 유니티 고유변수를 이용하여 transform.Rotate변수를 바꿔줍니다.
        transform.Rotate(new Vector3(10f, 20f, 30f) * Time.deltaTime);
    
        transform.Rotate(new Vector3(10f, 20f, 30f) * Time.deltaTime, Space.World);
    }
}
