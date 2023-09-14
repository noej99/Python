package com.noej.jul212wc.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// alt + shift + o

// Hadoop
//	서버급 컴 여러대로 병렬처리하는 Java프로그램
//	리눅스에서만 실행가능

//	왜 윈도우에서 작업?
//		자동완성
//	실제 실행할 리눅스에는 이미 다 있고
//	=> 자동완성에 필요한것만 넣어서 쓰고, 버리자
//	hadoop-common
//	hadoop-mapreduce-client-core
public class WCMain {
	public static void main(String[] args) {
		try {
			Configuration c = new Configuration();
			Job j = Job.getInstance(c);
			
			j.setMapperClass(WCMapper.class);
			j.setCombinerClass(WCReducer.class);
			j.setReducerClass(WCReducer.class);
			
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(IntWritable.class);
			
			// 원래 실행명령어
			// bin/hadoop	jar	파일명	
			// bin/hadoop	jar	파일명	대상	결과폴더
			FileInputFormat.addInputPath(j, new Path(args[0]));

			// 최상위의 rjResult라는 폴더에 결과를
			FileOutputFormat.setOutputPath(j, new Path(args[1]));
			
			// 작업끝날때까지 가만히
			j.waitForCompletion(true);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
