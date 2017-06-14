#include "stdafx.h"
#include <iostream>

using namespace std;
//以十个人七项任务为例

typedef struct CTNODE {
	double cost; //存放个人经费消耗
	int person_num;	//记录是第几人的选择层，值等于当前结点所在层次数-1
	int task_num; //记录是第几个任务，值等于母结点的从左往右的第几个子结点数
	int* travellist;	//记录是遍历过哪些任务，遍历的时候会用上
	double allcost; //记录总的费用，遍历的时候会用上
	CTNODE* child; //子结点
};
//创建并初始化树，给所有结点的person_num和task_num赋值
void createchildnode(CTNODE& parnode, int m, int n) {
	if (parnode.person_num < n) {
		parnode.child = new CTNODE[m + 1];
		for (int i = 1; i <= m; i++) {
			parnode.child[i].person_num = parnode.person_num + 1;
			parnode.child[i].task_num = i;
			parnode.child[i].travellist = new int[n];
			for (int j = 1; j <= n; j++) {
				parnode.travellist[j] = 0;
			}
			createchildnode(parnode.child[i], m, n);
		}
	}
}

//遍历树
void inittree(CTNODE& parnode, double cost[100][100], int n, int m,CTNODE* leafnode,int& leafnum) {	//需要提供一个根节点的引用，和cost矩阵
	//非叶子结点的情况
	bool travelvalue = 1;	//辅助变量，用于判断是否需要遍历该结点
	//如果子结点的task_num已经出现在母结点的travelist中，则不遍历该结点
	if (parnode.person_num <n) {
		for (int i = 1; i <= m; i++) {
			for (int j = 1; j <= n; j++) {
				if (parnode.child[i].task_num = parnode.travellist[j]) {
					travelvalue = 0;
					break;
				}
			}
			if (travelvalue == 1) {
				parnode.child[i].cost = cost[parnode.child[i].person_num][parnode.child[i].task_num];
				parnode.child[i].allcost = parnode.allcost + parnode.child[i].cost;
				parnode.child[i].travellist[parnode.child[i].person_num] = parnode.child[i].task_num;
				inittree(parnode.child[i], cost, n, m,leafnode,leafnum);
			}
			travelvalue = 1;
		}
	}

	//叶子结点的情况，存入辅助ctnode数组
	if (parnode.person_num == n) {

		leafnum++;
		leafnode[leafnum] = parnode;
	}
}



void sortcost(CTNODE* leafnode,int leafnum,int n) {
	CTNODE minleaf=leafnode[1];	//辅助变量，存放最优解
	for (int i = 2; i <= leafnum; i++) {
		if (minleaf.allcost < leafnode[i].allcost) {
			minleaf = leafnode[i];
		}
	}
	for (int j = 1; j <= n; j++) {
		cout << minleaf.travellist[j];
	}


}

//求阶乘工具
int jiecheng(int x) {
	int mul = 1;
	for (x; x >= 1; x--) {
		mul = mul*x;
	}
	return mul;
}


int main()
{
	////n个人，m个任务
	CTNODE rootnode;
	double cost[100][100];
	int m, n;
	cin >> n >> m;
	int test = 0;
	int i, j;
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= m; j++)
			cin >> cost[i][j];
	}
	rootnode.cost = 0; rootnode.person_num = 0; rootnode.task_num = 0;	//根结点的数据成员无实际意义，全设为0
	rootnode.allcost = 0; 
	rootnode.travellist = new int[n] ;
	for (int i = 1; i <= n; i++) {
		rootnode.travellist[i] = -1;
	}
	rootnode.child = new CTNODE[m + 1];
	createchildnode(rootnode, m,n);


	int leafsize = jiecheng(n) / jiecheng(n - m);
	CTNODE* leafnode = new CTNODE[leafsize+1];	//辅助CTNODE数组，存放所有的叶子结点
	int leafnum = 0;	//辅助变量，记录CTNODE中有多少个叶子结点
	inittree(rootnode, cost, n, m,leafnode,leafnum);
	sortcost(leafnode, leafnum, n);
	system("pause");
	return 0;
}
