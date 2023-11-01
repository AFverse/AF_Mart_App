import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:myfirstapp/screens/login_Screen.dart';

class SignUpScreen extends StatelessWidget {

   SignUpScreen({Key? key}) : super(key: key);
  final TextEditingController emailController = TextEditingController();
  final TextEditingController nameController = TextEditingController();
  final TextEditingController phoneController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: (){
            Navigator.pop(context);
          },
          icon: const Icon(Icons.arrow_back),
        ),
        backgroundColor: Colors.white,
        foregroundColor: Colors.black,
        elevation: 0,
        //title: const Text("Sign Up screen"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(12.0),
        child: Column(
          children: [
            SizedBox(
              height: MediaQuery.of(context).size.height*0.25,
              child: Image.asset("assets/images/sign_up.jpg"),
            ),
            const SizedBox(height: 10,),
             const Text ("Sign Up", style: TextStyle(fontSize: 45,fontWeight: FontWeight.w900),
             ),
             const SizedBox(height: 10,),
              TextField(
                controller: emailController,
                decoration: const InputDecoration(
                  border: UnderlineInputBorder(),
                  hintText: "Email",
                  icon: Icon(Icons.email)

                ),
              ),
              TextField(
                controller: nameController,
                decoration: const InputDecoration(
                    border: UnderlineInputBorder(),
                    hintText: "Full Name",
                    icon: Icon(Icons.person),

                ),
              ),
              TextField(
                controller: phoneController,
                decoration: const InputDecoration(
                    border: UnderlineInputBorder(),
                    hintText: "Mobile",
                    icon: Icon(Icons.phone)

                ),
              ),
            const SizedBox( height: 12,),
            Wrap(
              children: [
                const Text("By Signing Up, you are agree to our"),
              ],
            ),
            const SizedBox( height: 12,),
            SizedBox(
              width: double.maxFinite,
              height: 45,
              child: ElevatedButton(
                onPressed:(){

                } ,
                child: const Text("Continue"),
              ),
            ),
            const SizedBox( height: 12,),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Join us befofe?", style: TextStyle(color: Colors.grey),),
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
      )
    );
  }
}
