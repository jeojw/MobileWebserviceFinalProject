package com.example.myapplication.api;

import com.example.myapplication.model.ChangeImage;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface ApiService {
    @GET("list/")
    Call<List<ChangeImage>> getImages();
}
