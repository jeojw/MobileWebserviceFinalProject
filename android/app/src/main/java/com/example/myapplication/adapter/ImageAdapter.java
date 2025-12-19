package com.example.myapplication.adapter;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.myapplication.ImageDetailActivity;
import com.example.myapplication.R;
import com.example.myapplication.model.ChangeImage;

import java.util.List;

public class ImageAdapter extends RecyclerView.Adapter<ImageAdapter.ViewHolder> {

    Context ctx;
    List<ChangeImage> list;

    public ImageAdapter(Context ctx, List<ChangeImage> list) {
        this.ctx = ctx;
        this.list = list;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(ctx)
                .inflate(R.layout.item_image, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        ChangeImage item = list.get(position);
        holder.type.setText(item.change_type);

        Glide.with(ctx)
                .load("http://10.0.2.2:8000" + item.image)
                .into(holder.img);

        holder.itemView.setOnClickListener(v -> {
            Intent i = new Intent(ctx, ImageDetailActivity.class);
            i.putExtra("image_url", "http://10.0.2.2:8000" + item.image);
            ctx.startActivity(i);
        });
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        ImageView img;
        TextView type;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            img = itemView.findViewById(R.id.itemImageView);
            type = itemView.findViewById(R.id.itemType);
        }
    }
}
