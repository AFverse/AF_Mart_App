import 'package:flutter/material.dart';
import 'package:myfirstapp/screens/reset_password.dart';

import 'login_Screen.dart';

class OTPScreen extends StatelessWidget {
   OTPScreen({Key? key}) : super(key: key);

  final TextEditingController firstController = TextEditingController();
  final TextEditingController secondController = TextEditingController();
  final TextEditingController thirdController = TextEditingController();
  final TextEditingController fourthController = TextEditingController();
  final TextEditingController fifthController = TextEditingController();
  final TextEditingController sixthController = TextEditingController();


  @override
  Widget build(BuildContext context) {
    double size = MediaQuery.of(context).size.width * 0.15;
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.white,
        foregroundColor: Colors.black,
        elevation: 0,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            SizedBox(
              height: MediaQuery.of(context).size.height*0.25,
              child: Image.asset("assets/images/sign_up.jpg"),
            ),
            const SizedBox(height: 10,),
            const Align(
              alignment: Alignment.centerLeft,
              child:  Text ("Enter OTP", style: TextStyle(fontSize: 45,fontWeight: FontWeight.w900),
              ),
            ),

            const SizedBox(height: 10,),
            const Padding(
              padding: EdgeInsets.all(8.0),

              child: Align(
                alignment: Alignment.centerLeft,
                child: Text ("A 4 digit code has been sent to komalwaheed799@gmail.com")
                ),
              ),

            Padding(padding: const EdgeInsets.symmetric(vertical: 20.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                SizedBox(
                  width: size,
                  height: size,
                  child: TextField(
                    controller: firstController,
                    keyboardType: TextInputType.number,
                    textAlign: TextAlign.center,
                    cursorHeight: 25,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(4)),
                      )
                    ),
                     onChanged: (val){

                     },
                  ),
                ),
                SizedBox(
                  width: size,
                  height: size,
                  child: TextField(
                    controller: secondController,
                    keyboardType: TextInputType.number,
                    textAlign: TextAlign.center,
                    cursorHeight: 25,
                    decoration: const InputDecoration(
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(4)),
                        )
                    ),
                    onChanged: (val){
                            if(val.length>1)
                              {
                                secondController.text = val[0];
                                thirdController.text = val[1];
                              }
                    },
                  ),
                ),
                SizedBox(
                  width: size,
                  height: size,
                  child: TextField(
                    controller: thirdController,
                    keyboardType: TextInputType.number,
                    textAlign: TextAlign.center,
                    cursorHeight: 25,
                    decoration: const InputDecoration(
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(4)),
                        )
                    ),
                    onChanged: (val){
                      if(val.length>1)
                      {
                        thirdController.text = val[0];
                        fourthController.text = val[1];
                      }
                    },
                  ),
                ),
                SizedBox(
                  width: size,
                  height: size,
                  child: TextField(
                    controller: fourthController,
                    keyboardType: TextInputType.number,
                    textAlign: TextAlign.center,
                    cursorHeight: 25,
                    decoration: const InputDecoration(
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(4)),
                        )
                    ),
                    onChanged: (val){
                      if(val.length>1)
                      {
                        if(val.length>1)
                        {
                          fourthController.text = val[0];
                          fifthController.text = val[1];
                        }
                      }
                    },
                  ),
                ),

                SizedBox(
                  width: size,
                  height: size,
                  child: TextField(
                    controller: fifthController,
                    keyboardType: TextInputType.number,
                    textAlign: TextAlign.center,
                    cursorHeight: 25,
                    decoration: const InputDecoration(
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(4)),
                        )
                    ),
                    onChanged: (val){
                      if(val.length>1)
                      {
                 fifthController.text = val[0];
                 sixthController.text = val[1];
                      }
                    },
                  ),
                ),
                SizedBox(
                  width: size,
                  height: size,
                  child: TextField(
                    controller: firstController,
                    keyboardType: TextInputType.number,
                    textAlign: TextAlign.center,
                    cursorHeight: 25,
                    decoration: const InputDecoration(
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(4)),
                        )
                    ),

                  ),
                ),
              ],
            ),
            ),

            const SizedBox( height: 12,),
            Padding(
                padding: const EdgeInsets.all(10),
              child: SizedBox(
                height: 40,
                width: double.maxFinite,
                child: ElevatedButton(
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(Colors.blueAccent.shade700),
                    shape: MaterialStateProperty.all(
                      const RoundedRectangleBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10))
                      )
                    )
                  ),
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context) => Reset()));
                  },
                  child: const Text("Enter", style: TextStyle(fontWeight: FontWeight.w500),),
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [

                TextButton(
                    onPressed: (){
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) =>  LoginScreen()),
                      );
                    },
                    child: const Text("Login")
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}
