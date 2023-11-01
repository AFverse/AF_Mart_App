import 'package:flutter/material.dart';
import 'package:myfirstapp/screens/otpscreen.dart';
import 'package:myfirstapp/screens/register.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
bool isShowPassword = true;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("login Screen"),
      ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(12.0),
          child: Form(
            key: _formKey,
            child: Column(
              children: [
                SizedBox(
                  height: MediaQuery.of(context).size.height*0.25,
                  child: Image.asset("assets/images/login 1.png"),
                ),
                const SizedBox(height: 10,),
                const Text ("Login", style: TextStyle(fontSize: 45,fontWeight: FontWeight.w900),
                ),
                const SizedBox(height: 10,),
                TextFormField(
                  controller: emailController,
                  decoration: const InputDecoration(
                      border: UnderlineInputBorder(),
                      hintText: "Email ID/Phone No",
                      icon: Icon(Icons.alternate_email),
                  ),
                  validator: (val)
                  {
                    if(val!.isEmpty)
                      {
                        return "Please Enter Email ID";
                      }
                    if(!val.contains("@") || !val.contains("."))
                      {
                        return "Enter Valid Email ID";
                      }
                    return null;
                  },
                ),
                TextFormField(
                  readOnly: false,
                  obscureText: isShowPassword,
                  controller: passwordController,
                  decoration:  InputDecoration(
                    border:const UnderlineInputBorder(),
                    hintText: "Password",
                    icon: const Icon(Icons.lock),
                    suffixIcon: IconButton(
                        onPressed: (){
                          setState(() {
                            isShowPassword = !isShowPassword;
                          });
                        },
                        icon: isShowPassword == true ? const Icon(Icons.visibility) : const Icon(Icons.visibility_off),)
                    ),
                    validator: (val)
                  {
                    if(val!.isEmpty)
                      {
                        return "Please Enter Password";
                      }
                    else if(val.length < 8)
                      {
                        return "Enter Strong Password";
                      }

                    return null;
                  },
                  ),
                const SizedBox( height: 12,),
                Container(
                  alignment: Alignment.centerRight,
                  child: Wrap(

                    children: const [
                      Text("Forgot Password?", style: TextStyle(color: Colors.blue, ),
                      ),

                    ],

                  ),
                ),
                const SizedBox( height: 12,),
                SizedBox(
                  width: double.maxFinite,
                  height: 45,
                  child: ElevatedButton(
                    onPressed:(){
                      if(_formKey.currentState!.validate())
                        {
                          Navigator.push(context,MaterialPageRoute(builder:(context) => OTPScreen(), ));
                        }
                    } ,
                    child: const Text("Login", style: TextStyle(fontSize: 20),),
                  ),
                ),
                const SizedBox( height: 12,),

                const Text ("OR", style: TextStyle(fontSize: 15,fontWeight: FontWeight.w300, color: Colors.grey),
                ),
                const SizedBox( height: 12,),
                SizedBox(
                  width: double.maxFinite,
                  height: 45,
                  child: OutlinedButton.icon(

                    onPressed: () {},
                    icon: const Icon(
                      Icons.facebook,
                      size: 24.0,
                    ),
                    label: const Text('Login with Facebook', style: TextStyle(color: Colors.black),),
                  ),
                ),


                const SizedBox( height: 12,),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text("New to Logistics?", style: TextStyle(color: Colors.grey),),

                    //
                    TextButton(
                        onPressed: (){
                          Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => const RegisterScreen(),)
                          );
                        },
                        child: const Text("Register")
                    )



                  ],
                )
              ],
            ),
          ),
        ),
    );
  }
}