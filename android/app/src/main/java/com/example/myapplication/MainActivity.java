package com.example.myapplication;


import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.example.myapplication.adapter.ImageAdapter;
import com.example.myapplication.api.ApiService;
import com.example.myapplication.api.RetrofitInstance;
import com.example.myapplication.model.ChangeImage;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    ImageAdapter adapter;
    List<ChangeImage> list = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new ImageAdapter(this, list);
        recyclerView.setAdapter(adapter);

        loadImages();
    }

    private void loadImages() {
        RetrofitInstance.getApi().getImages().enqueue(new Callback<List<ChangeImage>>() {
            @Override
            public void onResponse(Call<List<ChangeImage>> call, Response<List<ChangeImage>> response) {
                if (response.isSuccessful() && response.body() != null) {
                    list.clear();
                    list.addAll(response.body());
                    adapter.notifyDataSetChanged();
                }
            }

            @Override
            public void onFailure(Call<List<ChangeImage>> call, Throwable t) {
                Log.e("API_ERROR", t.getMessage());
            }
        });
    }
}