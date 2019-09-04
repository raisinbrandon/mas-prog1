package com.example.helloworld;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ScrollView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button sendButton = (Button) findViewById(R.id.sendButton);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText messageEntryBox = (EditText) findViewById(R.id.messageEntryBox);
                TextView messageList = (TextView) findViewById(R.id.messageList);

                String text = messageEntryBox.getText().toString();
                messageList.setTextSize(TypedValue.COMPLEX_UNIT_SP, 27);
                messageList.setText(text);
            }
        });
    }
}
