import 'package:flutter/material.dart';

class Reset extends StatelessWidget {
   Reset({Key? key}) : super(key: key);
  final TextEditingController newPasswordController = TextEditingController();
  final TextEditingController createNewPasswordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Reset Password"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(12.0),
        child: Column(
          children: [
            SizedBox(
              height: MediaQuery.of(context).size.height*0.25,
              child: Image.asset("assets/images/login 1.png"),
            ),
            const SizedBox(height: 10,),
            const Text ("Reset Password", style: TextStyle(fontSize: 45,fontWeight: FontWeight.w900),
            ),
            const SizedBox(height: 10,),
            TextField(
              controller: newPasswordController,
              decoration: const InputDecoration(
                  border: UnderlineInputBorder(),
                  hintText: "New Password",
                  icon: Icon(Icons.lock)

              ),
            ),





            TextField(
                readOnly: false,
                obscureText: true,
                controller: createNewPasswordController,
                decoration:  InputDecoration(
                    border:const UnderlineInputBorder(),
                    hintText: "Create New password",

                    icon: const Icon(Icons.lock),
                )

            ),

            const SizedBox( height: 12,),
            const SizedBox( height: 12,),
            const SizedBox( height: 12,),
            const SizedBox( height: 12,),
            const SizedBox( height: 12,),
            // SizedBox(
            //  
            //   width: double.maxFinite,
            //   height: 45,
            //  
            //   child: OutlinedButton.icon(
            //
            //     onPressed: () {
            //      
            //     },
            //     icon: Icon(
            //      
            //       Icons.cached,
            //       size: 24.0,
            //     ),
            //    
            //     label: Text('Submitting', style: TextStyle(color: Colors.white),),
            //   ),
            //  
            // ),

            ElevatedButton(
                onPressed: (){}, 
                child: const Text("Submitting")
            )
            
      ]
      ),

    ),
    );
  }
}
